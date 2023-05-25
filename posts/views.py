from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

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
            return redirect('post:post_success')  # Redirect to the success page
    else:
        form = PostForm()

    return render(request, 'post/post_create.html', {'form': form})

@login_required(login_url='/accounts/login/')
def post_success(request):
    return render(request, 'post/post_success.html')
