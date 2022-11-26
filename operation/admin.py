from django.contrib import admin
from .models import AudienceInterest,AddName , Title,Body,FileName , ProductName,ProductImageHash,ApprovalName,StoryId,CallToAction


admin.site.register(AddName)
admin.site.register(AudienceInterest)

admin.site.register(Title)
admin.site.register(Body)

admin.site.register(FileName)
admin.site.register(ProductName)

admin.site.register(ProductImageHash)
admin.site.register(ApprovalName)

admin.site.register(StoryId)
admin.site.register(CallToAction)

