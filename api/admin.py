from django.contrib import admin
from .models import Campiagn,Audience,Platform,Placement,AddSetName,PageName,CampaignName,Retargeting,CampaignObjective,Engagement,ExcludedCustom,Code
# others
from .models import CampaignBidStrategy,AdSetRunStatus,InstagramPositions,FacebookPositions,MessengerPositions,AudienceNetworkPositions,OptimizationGoal,BillingEvent,AdSetBidStrategy,BuyingType,CampaignStatus , AdStatus , OculusPositions

# Register your models here.
admin.site.register(Campiagn)
admin.site.register(Audience)

admin.site.register(Platform)
admin.site.register(Placement)

admin.site.register(AddSetName)
admin.site.register(PageName)

admin.site.register(CampaignName)
admin.site.register(CampaignObjective)

admin.site.register(Retargeting)
admin.site.register(Engagement)

admin.site.register(ExcludedCustom)
admin.site.register(Code)


#Others
admin.site.register(CampaignBidStrategy)
admin.site.register(AdSetRunStatus)
admin.site.register(InstagramPositions)
admin.site.register(FacebookPositions)
admin.site.register(MessengerPositions)
admin.site.register(AudienceNetworkPositions)
admin.site.register(OptimizationGoal)
admin.site.register(BillingEvent)
admin.site.register(AdSetBidStrategy)
admin.site.register(BuyingType)
admin.site.register(CampaignStatus)
admin.site.register(AdStatus)
admin.site.register(OculusPositions)
