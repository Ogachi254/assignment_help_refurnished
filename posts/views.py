from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import user_passes_test
from .models import Post
from .forms import PostForm

def admin_check(user):
    return user.is_superuser

@login_required(login_url='/accounts/login/')
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})

@login_required(login_url='/accounts/login/')
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('post:post_success')
    else:
        form = PostForm()

    return render(request, 'post/post_create.html', {'form': form})

@login_required(login_url='/accounts/login/')
@user_passes_test(admin_check, login_url='/accounts/login/')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post:post_success')
    else:
        form = PostForm(instance=post)

    return render(request, 'post/post_edit.html', {'form': form, 'post': post})

@login_required(login_url='/accounts/login/')
@user_passes_test(admin_check, login_url='/accounts/login/')
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('post:post_list')
    return redirect('post:post_list')

@login_required(login_url='/accounts/login/')
def post_success(request):
    return render(request, 'post/post_success.html')
