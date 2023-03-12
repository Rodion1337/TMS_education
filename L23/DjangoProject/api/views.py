from django.shortcuts import render
from django.http import JsonResponse
from requests import request
from HW23.models import Games, Comments, Categories
from .serializers import GameSerializer, CommentsSerializer, CategoriesSerializer
from io import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from random import randint
# from rest_framework.serializers import Serializer

# Create your views here.

def api_games(request):
    if request.method == 'GET':
        games = Games.objects.all()
        game_serializer = GameSerializer(games, many=True).data
        content = JSONRenderer().render(game_serializer)
        stream = BytesIO(content)
        data = JSONParser().parse(stream)
        return JsonResponse (data, safe=False)

class GetGameInfoView(APIView):
    def get(self, request):
        queryset = Games.objects.all()
        if request.GET.get('random', False):
            queryset = queryset[randint(0, len(queryset))]
            serializer_for_queryset = GameSerializer(instance=queryset)
        else:
            queryset = queryset[0:5] #игр лишь 7, поэтому вывод 5 штук :)
            serializer_for_queryset = GameSerializer(instance=queryset, many=True)
        return Response({"games": serializer_for_queryset.data})


def api_comments(request):
    if request.method == 'GET':
        comment = Comments.objects.all()
        comment_serializer = CommentsSerializer(comment, many=True)
        return JsonResponse (comment_serializer.data, safe=False)


def api_categories(request):
    if request.method == 'GET':
        category = Categories.objects.all()
        category_serializer = CategoriesSerializer(category, many=True)
        return JsonResponse (category_serializer.data, safe=False)