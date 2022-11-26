from django.shortcuts import render
from rest_framework import generics
from .serializers import AudienceInterestSerializer,AddNameSerializer , TitleSerializer,BodySerializer,FileNameSerializer,ProductNameSerializer,ProductImageHashSerializer,ApprovalNameSerializer,StoryIdSerializer,CallToActionSerializer
from .models import AudienceInterest,AddName , Title,Body,FileName , ProductName,ProductImageHash,ApprovalName,StoryId,CallToAction

class AddNameList(generics.ListCreateAPIView):
    serializer_class = AddNameSerializer
    queryset = AddName.objects.all()

class AddNameDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddNameSerializer
    queryset = AddName.objects.all()

class AudienceInterestList(generics.ListCreateAPIView):
    serializer_class = AudienceInterestSerializer
    queryset = AudienceInterest.objects.all()

class AudienceInterestDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AudienceInterestSerializer
    queryset = AudienceInterest.objects.all()

class TitleList(generics.ListCreateAPIView):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()

class TitleDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TitleSerializer
    queryset = Title.objects.all()

class BodyList(generics.ListCreateAPIView):
    serializer_class = BodySerializer
    queryset = Body.objects.all()

class BodyDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BodySerializer
    queryset = Body.objects.all()

class ProductNametList(generics.ListCreateAPIView):
    serializer_class = ProductNameSerializer
    queryset = ProductName.objects.all()

class ProductNameDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductNameSerializer
    queryset = ProductName.objects.all()

class FileNameList(generics.ListCreateAPIView):
    serializer_class = FileNameSerializer
    queryset = FileName.objects.all()

class FileNameDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FileNameSerializer
    queryset = FileName.objects.all()

class ProductImageHashList(generics.ListCreateAPIView):
    serializer_class = ProductImageHashSerializer
    queryset = ProductImageHash.objects.all()

class ProductImageHashDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductImageHashSerializer
    queryset = ProductImageHash.objects.all()

class CallToActionList(generics.ListCreateAPIView):
    serializer_class = CallToActionSerializer
    queryset = CallToAction.objects.all()

class CallToActionDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CallToActionSerializer
    queryset = CallToAction.objects.all()

class StoryIdList(generics.ListCreateAPIView):
    serializer_class = StoryIdSerializer
    queryset = StoryId.objects.all()

class StoryIdDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StoryIdSerializer
    queryset = StoryId.objects.all()

class ApprovalNameList(generics.ListCreateAPIView):
    serializer_class = ApprovalNameSerializer
    queryset = ApprovalName.objects.all()

class ApprovalNameDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ApprovalNameSerializer
    queryset = ApprovalName.objects.all()





