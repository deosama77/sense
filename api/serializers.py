from rest_framework import  serializers
from .models import Audience,Campiagn,AddSetName,Platform,Placement,CampaignName,PageName,CampaignObjective,ExcludedCustom,Code,Engagement,Retargeting

class CampiagnSerializer(serializers.ModelSerializer):
    class Meta:
        model=Campiagn
        fields=('__all__')

class AudienceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Audience
        fields=('__all__')

class AddSetNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=AddSetName
        fields=('__all__')

class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Placement
        fields=('__all__')

class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model=Platform
        fields=('__all__')

class CampaignNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=CampaignName
        fields=('__all__')

class PageNameSerializer(serializers.ModelSerializer):
    class Meta:
        model=PageName
        fields=('__all__')

class CampaignObjectiveSerializer(serializers.ModelSerializer):
    class Meta:
        model=CampaignObjective
        fields=('__all__')

class RetargetingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Retargeting
        fields=('__all__')

class EngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model=Engagement
        fields=('__all__')

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Code
        fields=('__all__')

class ExcludedCustomSerializer(serializers.ModelSerializer):
    class Meta:
        model=ExcludedCustom
        fields=('__all__')