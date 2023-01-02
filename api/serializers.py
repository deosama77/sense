from rest_framework import  serializers
from .models import Audience,Campiagn,AddSetName,Platform,Placement,CampaignName,PageName,CampaignObjective,ExcludedCustom,Code,Engagement,Retargeting
# others
from .models import CampaignBidStrategy,AdSetRunStatus,InstagramPositions,FacebookPositions,MessengerPositions,AudienceNetworkPositions,OptimizationGoal,BillingEvent,AdSetBidStrategy,BuyingType,CampaignStatus ,AdStatus , OculusPositions

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

# Other ..................................................................
class CampaignStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=CampaignStatus
        fields=('__all__')

class AdSetRunStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdSetRunStatus
        fields=('__all__')

class CampaignBidStrategySerializer(serializers.ModelSerializer):
    class Meta:
        model=CampaignBidStrategy
        fields=('__all__')

class InstagramPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=InstagramPositions
        fields=('__all__')


class FacebookPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=FacebookPositions
        fields=('__all__')

class AudienceNetworkPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=AudienceNetworkPositions
        fields=('__all__')


class OptimizationGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model=OptimizationGoal
        fields=('__all__')

class BillingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model=BillingEvent
        fields=('__all__')

class MessengerPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=MessengerPositions
        fields=('__all__')

class AdSetBidStrategySerializer(serializers.ModelSerializer):
    class Meta:
        model=AdSetBidStrategy
        fields=('__all__')

class BuyingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=BuyingType
        fields=('__all__')

class AdStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model=AdStatus
        fields=('__all__')

class OculusPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model=OculusPositions
        fields=('__all__')