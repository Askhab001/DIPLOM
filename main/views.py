from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Command
from .forms import CommandForm


def index(request):
    return render(request, 'main.html')


def main(request):
    return render(request, 'aza1.html')


def aza(request):
    return render(request, 'aza2.html')


def asa(request):
    return render(request, 'aza3.html')


@login_required
def create_command(request):
    if request.method == 'POST':
        form = CommandForm(request.POST)
        if form.is_valid():
            command = form.save(commit=False)
            command.author = request.user
            command.save()
            return redirect('command_list')
    else:
        form = CommandForm()
    return render(request, 'command1.html', {'form': form})


def command_list(request):
    commands = Command.objects.all()
    return render(request, 'command.html', {'command': commands})