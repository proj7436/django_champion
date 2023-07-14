from rest_framework import serializers
from .models import Key

class GetAPISerializers(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ('key', )



class PostKeySerializers(serializers.Serializer):
    key =serializers.CharField(max_length = 255)
    class_key = serializers.CharField(max_length = 20)

