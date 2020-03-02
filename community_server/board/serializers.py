from board.models import Board
from rest_framework import serializers

class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('id','title','writer','writer_ip','datetime','tag','post_hit','thumbnail')

class BoardUpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('id','title','content','writer','thumbnail')

class BoardDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('id','title','content','writer','writer_ip','datetime','tag','post_hit')

class BoardCreateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('id','title','content','writer','password','tag')