from django.contrib import admin
from .models import Campiagn,Audience,Platform,Placement,AddSetName,PageName,CampaignName,Retargeting,CampaignObjective,Engagement,ExcludedCustom,Code

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
