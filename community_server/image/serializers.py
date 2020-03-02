from image.models import UploadFileModel
from rest_framework import serializers

class ImgSerializer(serializers.ModelSerializer):
    upload = serializers.ImageField(use_url=True)
    class Meta:
        model = UploadFileModel
        fields = ('upload',)
    
    
