from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    posts = Post.objects.all()
    form = PostForm()
    context = {'posts': posts, 'form': form}
    return render(request, 'todo/index.html', context) 

def create(request):
    form = PostForm(request.POST)
    form.save(commit=True)
    return HttpResponseRedirect(reverse('todo:index')) # todo一覧にリダイレクトできる
    
def delete(request, id=None): # urls.pyで設定したidがここに来る
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return HttpResponseRedirect(reverse('todo:index'))
    
