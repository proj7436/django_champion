from rest_framework import serializers
from .models import Key, SourceCode

class GetAPISerializers(serializers.ModelSerializer):
    class Meta:
        model = Key
        fields = ('key', )



class PostKeySerializers(serializers.Serializer):
    key =serializers.CharField(max_length = 255)
    class_key = serializers.CharField(max_length = 20)



class GetAPISourceCodeSerializers(serializers.ModelSerializer):
    class Meta:
        model = SourceCode
        fields = ('code', )


class PostAPISourceCodeSerializers(serializers.Serializer):
    code = serializers.CharField()  # Định nghĩa trường code là TextField
    key_update = serializers.CharField(max_length = 100)
