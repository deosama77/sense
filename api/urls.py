from django.urls import path
from .views import CampiagnList,CampiagnDetails , AudienceList , AudienceDetails , \
    AddSetNameList , AddSetNameDetails ,CodeList,CodeDetails , PlatformList,PlatformDetails,PlacementDetails,PlacementList ,\
    RetargetingList,RetargetingDetails ,ExcludedCustomList , ExcludedCustomDetails ,EngamentList,EngamentDetails,\
    CampaignNameList,CampaignNameDetails , CampaignObjectiveList,CampaignObjectiveDetails,PageNameList,PageNameDetails,export_to_excel


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
]