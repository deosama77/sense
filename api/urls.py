from django.urls import path
from .views import CampiagnList,CampiagnDetails , AudienceList , AudienceDetails , \
    AddSetNameList , AddSetNameDetails ,CodeList,CodeDetails , PlatformList,PlatformDetails,PlacementDetails,PlacementList ,\
    RetargetingList,RetargetingDetails ,ExcludedCustomList , ExcludedCustomDetails ,EngamentList,EngamentDetails,\
    CampaignNameList,CampaignNameDetails , CampaignObjectiveList,CampaignObjectiveDetails,PageNameList,PageNameDetails,export_to_excel

from .views import CampaignStatusList,CampaignStatusDetails , AdSetRunStatusList , AdSetRunStatusDetails , CampaignBidStrategyList , CampaignBidStrategyDetails , InstagramPositionsList , InstagramPositionsDetails , FacebookPositionsList , FacebookPositionsDetails  ,\
    MessengerPositionsList ,MessengerPositionsDetails ,AudienceNetworkPositionsList , AudienceNetworkPositionsDetails , OptimizationGoalList, OptimizationGoalDetails , BillingEventList , BillingEventDetails , AdSetBidStrategyList , AdSetBidStrategyDetails , BuyingTypeList , BuyingTypeDetails , AdStatusList , AdStatusDetails , OculusPositionsList , OculusPositionsDetails

urlpatterns = [
    path('campaign', CampiagnList.as_view()),
    path('campaign/<int:pk>', CampiagnDetails.as_view()),

    path('code', CodeList.as_view()),
    path('code/<int:pk>', CodeDetails.as_view()),

    path('platform', PlatformList.as_view()),
    path('platform/<int:pk>', PlatformDetails.as_view()),

    path('placement', PlacementList.as_view()),
    path('placement/<int:pk>', PlacementDetails.as_view()),

    path('page_name', PageNameList.as_view()),
    path('page_name/<int:pk>', PageNameDetails.as_view()),

    path('campaign_name', CampaignNameList.as_view()),
    path('campaign_name/<int:pk>', CampaignNameDetails.as_view()),

    path('campaign_objective', CampaignObjectiveList.as_view()),
    path('campaign_objective/<int:pk>', CampaignObjectiveDetails.as_view()),

    path('retargeting', RetargetingList.as_view()),
    path('retargeting/<int:pk>', RetargetingDetails.as_view()),

    path('engagement', EngamentList.as_view()),
    path('engagement/<int:pk>', EngamentDetails.as_view()),

    path('add_set_name', AddSetNameList.as_view()),
    path('add_set_name/<int:pk>', AddSetNameDetails.as_view()),

    path('audience', AudienceList.as_view()),
    path('audience/<int:pk>', AudienceDetails.as_view()),

    path('exclude_custom', ExcludedCustomList.as_view()),
    path('exclude_custom/<int:pk>', ExcludedCustomDetails.as_view()),

    path('export_to_excel',export_to_excel),

#     other ...................................

    path('campaign_status', CampaignStatusList.as_view()),
    path('campaign_status/<int:pk>', CampaignStatusDetails.as_view()),

    path('ad_set_run_status', AdSetRunStatusList.as_view()),
    path('ad_set_run_status/<int:pk>', AdSetRunStatusDetails.as_view()),

    path('campaign_bid_strategy', CampaignBidStrategyList.as_view()),
    path('campaign_bid_strategy/<int:pk>', CampaignBidStrategyDetails.as_view()),

    path('instagram_positions', InstagramPositionsList.as_view()),
    path('instagram_positions/<int:pk>', InstagramPositionsDetails.as_view()),

    path('facebook_positions', FacebookPositionsList.as_view()),
    path('facebook_positions/<int:pk>', FacebookPositionsDetails.as_view()),

    path('messenger_positions', MessengerPositionsList.as_view()),
    path('messenger_positions/<int:pk>', MessengerPositionsDetails.as_view()),

    path('audience_network_positions', AudienceNetworkPositionsList.as_view()),
    path('audience_network_positions/<int:pk>', AudienceNetworkPositionsDetails.as_view()),

    path('optimization_goal', OptimizationGoalList.as_view()),
    path('optimization_goal/<int:pk>', OptimizationGoalDetails.as_view()),

    path('billing_event', BillingEventList.as_view()),
    path('billing_event/<int:pk>', BillingEventDetails.as_view()),

    path('ad_set_bid_strategy', AdSetBidStrategyList.as_view()),
    path('ad_set_bid_strategy/<int:pk>', AdSetBidStrategyDetails.as_view()),

    path('buying_type', BuyingTypeList.as_view()),
    path('buying_type/<int:pk>', BuyingTypeDetails.as_view()),

    path('ad-status', AdStatusList.as_view()),
    path('ad_status/<int:pk>', AdStatusDetails.as_view()),

    path('oculus_positions', OculusPositionsList.as_view()),
    path('oculus_positions/<int:pk>', OculusPositionsDetails.as_view()),
]