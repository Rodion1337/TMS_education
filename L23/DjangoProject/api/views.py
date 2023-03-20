from django.shortcuts import render
from django.core.paginator import Paginator
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
    '''
    Данная в зависимости от передаваемых параметров осуществляет передачу необходимых данных в формате  json.
    Поддерживаемые ключи:
    sort - сортировка данных, по умолчанию данные выдаются без сортировки,
        поддерживается сортировка по цене (price) и названию (name)
    year - сортировка игр вышедших в определенном году
    random - при значение true передает одну случайную игру
    пагинация - вывод раздробленных отсортированных данных по желаемому количеству частями:
        page - номер страницы / части (по умолчания 1)
        amount - количество записей в 1 части / странице (по умолчанию 5)
    '''
    def get(self, request):
        request_result = request.GET
        
        sorted_order = {
            'None': Games.objects.all(),
            'price': Games.objects.order_by('price'),
            'name': Games.objects.order_by('name'),
        }
        sorted_game = request_result.get('sort', 'None')
        year = request_result.get('year')
        pages = request_result.get('page', 1)
        amount = request_result.get('amount', 5)
        queryset = sorted_order.get(sorted_game)
        if year:
            queryset = queryset.filter(release_date__year=int(year)) 
        page = Paginator(queryset, amount,0,True).get_page(pages)
        if request_result.get('random', False) == 'true':
            queryset = queryset[randint(0, len(queryset))]
            serializer_for_queryset = GameSerializer(instance=queryset)
        else:
            queryset = page
            serializer_for_queryset = GameSerializer(instance=queryset, many=True)
        return Response({"games": serializer_for_queryset.data})

class GetCommentInfoView(APIView):
    def get(self, request):
        if request.method == 'GET':
            comment = Comments.objects.all()
            comment_serializer = CommentsSerializer(instance=comment, many=True)
            # return JsonResponse (comment_serializer.data, safe=False)
            return Response({"comments": comment_serializer.data})


def api_categories(request):
    if request.method == 'GET':
        category = Categories.objects.all()
        category_serializer = CategoriesSerializer(category, many=True)
        return JsonResponse (category_serializer.data, safe=False)