from rest_framework import  serializers
from .models import AudienceInterest,AddName , Title,Body,FileName , ProductName,ProductImageHash,ApprovalName,StoryId,CallToAction

class AddNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddName
        fields=('__all__')

class AudienceInterestSerializer(serializers.ModelSerializer):
    class Meta:
        model=AudienceInterest
        fields=('__all__')

class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('__all__')

class BodySerializer(serializers.ModelSerializer):
    class Meta:
        model = Body
        fields = ('__all__')

class FileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileName
        fields = ('__all__')

class ProductNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductName
        fields = ('__all__')

class ProductImageHashSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImageHash
        fields = ('__all__')

class CallToActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallToAction
        fields = ('__all__')

class StoryIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryId
        fields = ('__all__')

class ApprovalNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalName
        fields = ('__all__')
