from rest_framework import serializers

from .models import Coach, Team, Player, Tournament, Game

class CoachSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coach
        fields = ('id','coach_name',)

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('id','team_name', 'average_score', 'coach','players',)

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id','player_name', 'player_height', 'average_score', 'no_of_games', 'team',)

class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournament
        fields = ('id','tournament_name','start_date','end_date','rounds','games',)

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id','tournament','game_date','home_team','away_team','home_team_score','away_team_score','home_team_from_game','away_team_from_game','winner','round_number',)