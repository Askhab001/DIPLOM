from django.urls import path
from .views import (
    TournamentListView,
    TournamentDetailView,
    TournamentCreateView,
    TournamentUpdateView,
    TournamentDeleteView
)

urlpatterns = [
    path('', TournamentListView.as_view(), name='A!'),
    path('tournament/<int:pk>/', TournamentDetailView.as_view(), name='command1'),
    path('tournament/new/', TournamentCreateView.as_view(), name='command'),
    path('tournament/<int:pk>/edit/', TournamentUpdateView.as_view(), name='A2'),
    path('tournament/<int:pk>/delete/', TournamentDeleteView.as_view(), name='tournament_delete'),
]

