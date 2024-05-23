# tournaments/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Tournament, Participant, Schedule, Result
from .forms import TournamentForm, ParticipantForm, ScheduleForm, ResultForm
from django.contrib.auth.decorators import login_required


@login_required
def tournament_create(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST)
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.organizer = request.user
            tournament.save()
            return redirect('command')
    else:
        form = TournamentForm()
    return render(request, 'command.html', {'form': form})


class TournamentListView(ListView):
    model = Tournament
    template_name = 'command1.html'
    context_object_name = 'tournaments'


class TournamentDetailView(DetailView):
    model = Tournament
    template_name = 'command1.html'
    context_object_name = 'tournament'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['participants'] = Participant.objects.filter(tournament=self.object)
        context['schedule'] = Schedule.objects.filter(tournament=self.object)
        context['results'] = Result.objects.filter(tournament=self.object)
        return context


class TournamentCreateView(CreateView):
    model = Tournament
    form_class = TournamentForm
    template_name = 'A!.html'
    success_url = reverse_lazy('tournament_list')

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)


class TournamentUpdateView(UpdateView):
    model = Tournament
    form_class = TournamentForm
    template_name = 'command.html'
    success_url = reverse_lazy('tournament_list')


class TournamentDeleteView(DeleteView):
    model = Tournament
    template_name = 'command1.html'
    success_url = reverse_lazy('tournament_list')
