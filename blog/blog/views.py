from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Category
from .forms import PostForm
from django.shortcuts import get_object_or_404

class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    ordering = ['-data_post']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/single.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')

class CommentCreateView(CreateView):
    model = Comment
    fields = ['autor', 'texto'] 
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.kwargs['pk']})

class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'
    context_object_name = 'categorias'

class CategoryDetailView(ListView):
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    def get_queryset(self):
        self.categoria = get_object_or_404(Category, pk=self.kwargs['pk'])
        return self.categoria.posts.all().order_by('-data_post') 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categoria_atual'] = self.categoria
        return context
    