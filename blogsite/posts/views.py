from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
from .ai_helper import generate_summary

def posts_list(request):
    posts=Post.objects.all()
    return render(request, 'posts/list.html', {'posts' : posts})


def posts_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'posts/detail.html', {'post': post})

@login_required
def posts_create(request):
    if request.method=='POST':
        Post.objects.create(
            author= request.user,
            title=request.POST['title'],
            content=request.POST['content'],
            category=request.POST['category']
        )
        return redirect('posts_list')

    return render(request, 'posts/form.html')

@login_required
def posts_update(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if post.author!= request.user:
         return redirect('posts_list')
    if request.method=='POST':
            post.title=request.POST['title']
            post.content=request.POST['content']
            post.category=request.POST['category']
            post.save()
            return redirect('posts_list')

    return render(request, 'posts/form.html', {'post': post})

@login_required
def posts_delete(request,pk):
    postss=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        postss.delete()
        return redirect('posts_list')

    return render(request, 'posts/delete.html' ,{'postss': postss})



@login_required
def posts_summary(request, pk):
    post = get_object_or_404(Post, pk=pk)
    summary = generate_summary(post.content)

    return render(request, 'posts/summary.html', {
        'post':    post,
        'summary': summary,
    })