from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'home.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class PostCreateView(CreateView):
    model = Post
    template_name = 'post_create.html'
    fields = '__all__'
    # def blog_detail_view(request, primary_key):
    #     post = Post.objects.get(pk=primary_key)
    #     except Post.DoesNotExist:
    #         raise Http404('Post does not exist')

    #     return render(request, 'post_detail.html', context={'post': post})


class PostUpdateView(UpdateView):
    model = Post
    fields = ['title']
    template_name = 'post_edit.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy("posts") # needs to match name in urlpatterns
