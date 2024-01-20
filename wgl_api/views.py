from django.shortcuts import get_object_or_404

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework import generics

from .utils import calculate_elo, create_match

from .models import (
    Game,
    Match,
    Player,
    Challenge,
)

from .serializers import (
    FullGameSerializer,
    MatchSerializer,
    PlayerSerializer,
    ChallengeSerializer,
)

class PlayerList(generics.ListCreateAPIView):
    serializer_class = PlayerSerializer
    
    def get_queryset(self):
        queryset = Player.objects.all() 
        
        discord_id = self.request.query_params.get("discord_id", None)
        if discord_id is not None:
            queryset = queryset.filter(discord_id=discord_id)
            
        return queryset

class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlayerSerializer

    def get_object(self):
        discord_id = self.kwargs.get('discord_id')
        return get_object_or_404(Player, discord_id=discord_id)
    
    def update(self, request, *args, **kwargs):
        
        player = self.get_object()
        
        queueing_for = request.data.get("queueing_for")
        
        queueing_for_game = Game.objects.get(game_id=queueing_for)
        
        if queueing_for is not None:
            
            # is another player queueing for this game?
            # if so, start a match with both players
            
            other_player = Player.objects.filter(queueing_for=queueing_for).first()
            
            if other_player is not None:
                
                # start a match with both players
                match = create_match(player, other_player, queueing_for_game)
                                                
                # return the match
                # TODO: we need a more permanent way to do this
                return Response(MatchSerializer(match).data, status=status.HTTP_201_CREATED)
        
        return super(PlayerDetail, self).update(request, *args, **kwargs)
    
class MatchList(generics.ListCreateAPIView):
    serializer_class = MatchSerializer
    
    def get_queryset(self):
        queryset = Match.objects.all() 
        
        game_id = self.request.query_params.get("game_id", None)
        if game_id is not None:
            queryset = queryset.filter(game=game_id)
            
        return queryset

class MatchDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MatchSerializer

    def get_object(self):
        match_id = self.kwargs.get('match_id')
        return get_object_or_404(Match, match_id=match_id)
    
    # we need to override the update method to check for a change in result
    def update(self, request, *args, **kwargs):
        
        match = self.get_object()

        # check if result was updated by the request
        result = request.data.get("result")

        
        if result is not None:
            
            print('tentative result is not none')
                        
            # if we are entering a result for this match for the first time
            if match.result == "" or match.result is None:
                
                print('stored result is empty')
                
                # update the result then calculate elo
                match.result = result
                match.save()
                calculate_elo(match)
                
            else:
                
                # retroactive result change procedure, just pass for now
                pass
            
        return super(MatchDetail, self).update(request, *args, **kwargs) 

    
class ChallengeList(generics.ListCreateAPIView):
    serializer_class = ChallengeSerializer
    
    def get_queryset(self):
        queryset = Challenge.objects.filter(accepted=None) 
        
        game_id = self.request.query_params.get("game_id", None)
        if game_id is not None:
            queryset = queryset.filter(game=game_id)
            
        return queryset
    
class ChallengeDetail(generics.RetrieveDestroyAPIView):
    serializer_class = ChallengeSerializer
    
    def get_object(self):
        challenge_id = self.kwargs.get('challenge_id')
        return get_object_or_404(Challenge, challenge_id=challenge_id)