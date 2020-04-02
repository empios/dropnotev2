from django.utils import timezone
from .models import Post, Files
from django.shortcuts import get_object_or_404
from .forms import PostForm, UrlForm
from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage


# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    posts.filter(published_date=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_delete(request, pk):
    Post.objects.get(pk=pk).delete()
    return redirect('/')


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def signup(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:
        form = RegisterForm()
    return render(response, "blog/signup.html", {'form': form})


def upload(request):
    context = {}
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        form = UrlForm(request.POST)
        item = form.save(commit=False)
        item.title = uploaded_file.name
        item.author = request.user
        item.url = fs.url(name)
        item.save()
    return render(request, 'upload.html', context)


def files_list(request):
    files = Files.objects.all()
    return render(request, 'blog/file_list.html', {'files': files})
