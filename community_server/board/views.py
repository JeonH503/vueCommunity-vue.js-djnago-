from rest_framework import viewsets,status
from board.serializers import BoardSerializer,BoardDetailSerializer,BoardCreateSerializer,BoardUpdateSerializer
from board.models import Board
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView
from bs4 import BeautifulSoup
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django import forms
class board_restful_main(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_queryset(self):
        qs = super().get_queryset().order_by('-datetime')

        search = self.request.query_params.get('search','')
        cat = self.request.query_params.get('cat','')
        if cat :
            if search : 
                qs = qs.filter(
                    Q(tag=cat) ,
                    Q(title__icontains=search) |
                    Q(content__icontains=search) |
                    Q(writer__icontains=search)
                ).distinct()
            else :
                qs = qs.filter(tag=cat)
        return qs

class board_restful_new(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_queryset(self):
        qs = super().get_queryset().order_by('-datetime')
        cat = self.request.query_params.get('cat','')
        qs = qs.filter(tag=cat)
        return qs[:5]


class board_restful_hot(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def get_queryset(self):
        time = timezone.now()
        oneWeekBefore = time - timezone.timedelta(days=6)
        qs = super().get_queryset().order_by('-post_hit')
        qs = qs.filter(datetime__gte=oneWeekBefore)
        return qs[:5]


class board_restful_detail(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer

class board_restful_update(UpdateAPIView):
    lookup_field = 'id'
    queryset = Board.objects.all()
    serializer_class = BoardUpdateSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        if instance.password != self.request.data['passwordChk']:
            return Response("passwordError",status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

class board_restful_updatePostHit(UpdateAPIView):
    lookup_field = 'id'
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.post_hit += 1
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
        

class board_restful_delete(DestroyAPIView):
    lookup_field = 'id'
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def delete(self, request, *args, **kwargs):
        if self.get_object().password != self.request.data['password']:
            return Response("passwordError",status=status.HTTP_400_BAD_REQUEST)
        return self.destroy(request, *args, **kwargs)
    
class board_restful_create(ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer

    def perform_create(self, serializer):
        bsObject = ''
        password = make_password('6126') # 나중에 감출 데이터
        ip = self.request.META.get('REMOTE_ADDR')
        content = self.request.data['content']
        tag = self.request.data['tag']
        bsObject = BeautifulSoup(content, "html.parser")
        secondDotIndex = ip.find('.' ,4)
        shortIp = ip[0:secondDotIndex]
        if tag == 'notice' :
            if check_password(self.request.data['password'],password):
                if bsObject.img:
                    serializer.save(writer_ip=shortIp,thumbnail = str(bsObject.img))
                else :
                    serializer.save(writer_ip=shortIp,thumbnail = '')
            else :
                raise forms.ValidationError('admin만 사용할수 있습니다')
        else:
            if bsObject.img:
                serializer.save(writer_ip=shortIp,thumbnail = str(bsObject.img))
            else :
                serializer.save(writer_ip=shortIp,thumbnail = '')