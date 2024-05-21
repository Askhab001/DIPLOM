from django.shortcuts import render
from .forms import PostForm
from .models import Tournament, Participant, Schedule, Result


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
    posts = LOL.objects.all()
    return render(request, 'A2.html', {'posts': posts})


def apa(request):
    return render(request, 'A1.html')


def tournament_list(request):
    tournaments = Tournament.objects.all()
    return render(request, 'command.html', {'tournaments': tournaments})


def tournament_detail(request, pk):
    tournament = Tournament.objects.get(pk=pk)
    participants = Participant.objects.filter(tournament=tournament)
    schedule = Schedule.objects.get(tournament=tournament)
    results = Result.objects.filter(tournament=tournament)
    return render(request, 'command1.html',
                  {'tournament': tournament, 'participants': participants, 'schedule': schedule, 'results': results})
