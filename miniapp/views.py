from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import Post
from django.views.generic import ListView,DetailView
from .forms import PostForm, Post_ByForm
from django.views import View

# Create your views here.
class home(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='blog/home.html'
    paginate_by=3
    
    

class postpage(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='blog/allpost.html'




class post_detail(DetailView):
    model = Post
    context_object_name = 'posts'
    template_name='blog/postdetail.html'
    slug_url_kwarg='slug'


class CreatePostView(View):
    def get(self, request):
        post_form = PostForm()
        post_by_form = Post_ByForm()
        return render(request, 'blog/adddata.html', 
            {'post_form': post_form, 
             'post_by_form': post_by_form
            })
    
    def post(self, request):
        post_form = PostForm(request.POST, request.FILES)
        post_by_form = Post_ByForm(request.POST)
        if post_form.is_valid() and post_by_form.is_valid():
            post_by = post_by_form.save()
            post = post_form.save(commit=False)
            post.posted_by = post_by
            post.save()
            return HttpResponseRedirect('/success')
        return render(request, 'blog/adddata.html', {'post_form': post_form, 'post_by_form': post_by_form})
    
    
class success(ListView):
    model = Post
    context_object_name = 'posts'
    template_name='blog/successful.html'