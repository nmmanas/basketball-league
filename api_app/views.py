#from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import TournamentSerializer, GameSerializer, PlayerSerializer, TeamSerializer, CoachSerializer
from .models import Tournament, Game, Player, Team, Coach


class TournamentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer

class GameViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Game.objects.all()
    serializer_class = GameSerializer

class PlayerViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

class TeamViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class CoachViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
