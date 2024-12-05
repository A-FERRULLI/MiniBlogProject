from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .forms import CreatePost, EditPost, AddComment, EditComment
from django.http.request import HttpRequest
from django.http.response import Http404
from .models import Post, Comment
from django.urls import reverse

# Create your views here.
def listPosts(request: HttpRequest):
    posts = Post.objects.all()
    return render(request, 'listPosts.html', {'posts': posts, 'form': CreatePost()})

def viewPost(request: HttpRequest, id: int):
    post = get_object_or_404(Post, pk=id)
    try: comments = get_list_or_404(Comment, post=post.pk)
    except Http404: comments = []
    return render(request, 'viewPost.html', {'post': post, 'comments': comments, 'form': AddComment()})

def createPost(request: HttpRequest):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            Post(title=title, content=content).save()
        else: return redirect(reverse('CreatePost'))
    return redirect(reverse('ListPosts'))

def editPost(request: HttpRequest, id: int):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = EditPost(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.content = form.cleaned_data['content']
            post.save()
            return redirect(reverse('ViewPost', kwargs={'id': id}))
    return render(request, 'editPost.html', {'post': post, 'form': EditPost(initial={'title': post.title, 'content': post.content})})

def deletePost(request: HttpRequest, id: int):
    get_object_or_404(Post, pk=id).delete()
    return redirect(reverse('ListPosts'))

def addComment(request: HttpRequest, id: int):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'POST':
        form = AddComment(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            text = form.cleaned_data['text']
            Comment(post=post, author=author, text=text).save()
        return redirect(reverse('ViewPost', kwargs={'id': id}))
    return redirect(reverse('ListPosts'))

def editComment(request: HttpRequest, id: int):
    comment = get_object_or_404(Comment, pk=id)
    postID = comment.post.pk
    if request.method == 'POST':
        form = EditComment(request.POST)
        if form.is_valid():
            comment.author = form.cleaned_data['author']
            comment.text = form.cleaned_data['text']
            comment.save()
            return redirect(reverse('ViewPost', kwargs={'id': postID}))
    return render(
        request,
        'editComment.html',
        {
            'comment': comment,
            'form': EditComment(initial={'author': comment.author, 'text': comment.text}),
            'postID': postID
        }
    )

def deleteComment(request: HttpRequest, id: int):
    comment = get_object_or_404(Comment, pk=id)
    postID = comment.post.pk
    comment.delete()
    return redirect(reverse('ViewPost', kwargs={'id': postID}))
