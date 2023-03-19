from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from HW23.models import Games, Comments, Categories

class GameSerializer(ModelSerializer):
    class Meta:
        model = Games
        fields = ('id', 'name', 'release_date', 'price', 'slug', 'description', 'rating_avg',)


class CommentsSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = ('game.name', 'author', 'title', 'content', 'rating',)


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = ('title', 'description', 'game_amount',)