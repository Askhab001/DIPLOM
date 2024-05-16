from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post


def lord(request):
    return render(request, 'reg.html')


def ford(request):
    return render(request, 'ford.html')


def main(request):
    return render(request, 'aza1.html')


def aza(request):
    return render(request, 'aza2.html')


def asa(request):
    return render(request, 'aza3.html')


def ada(request):
    return render(request, 'command1.html')


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('command1')
    else:
        form = PostForm()
    return render(request, 'command.html', {'form': form})


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'command1.html', {'posts': posts})
