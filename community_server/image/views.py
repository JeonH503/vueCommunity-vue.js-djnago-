from rest_framework import viewsets,status
from .serializers import ImgSerializer
from .models import UploadFileModel
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

class image_view_set(viewsets.ModelViewSet):
    queryset = UploadFileModel.objects.all()
    serializer_class = ImgSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        print(serializer.data['upload'])
        return Response({
            "uploaded" : 1,
            "fileName" : serializer.data['upload'],
            "url": serializer.data['upload']
            }, status=status.HTTP_201_CREATED, headers=headers)