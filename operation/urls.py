from django.urls import path
from .views import AddNameList,AddNameDetails,AudienceInterestList,AudienceInterestDetails,\
    TitleList,TitleDetails,BodyList,BodyDetails,ProductNametList,ProductNameDetails ,ProductImageHashList,ProductImageHashDetails,CallToActionList,\
    CallToActionDetails,StoryIdList,StoryIdDetails ,ApprovalNameList,ApprovalNameDetails,FileNameList,FileNameDetails
urlpatterns = [
    path('add_name', AddNameList.as_view()),
    path('add_name/<int:pk>/', AddNameDetails.as_view()),

    path('audience_interest', AudienceInterestList.as_view()),
    path('audience_interest/<int:pk>/', AudienceInterestDetails.as_view()),

    path('title', TitleList.as_view()),
    path('title/<int:pk>/', TitleDetails.as_view()),

    path('body', BodyList.as_view()),
    path('body/<int:pk>/', BodyDetails.as_view()),

    path('fill_name', FileNameList.as_view()),
    path('filt_name/<int:pk>/', FileNameDetails.as_view()),

    path('product_image_hash', ProductImageHashList.as_view()),
    path('product_image_hash/<int:pk>/', ProductImageHashDetails.as_view()),

    path('product_name', ProductNametList.as_view()),
    path('product_name/<int:pk>/', ProductNameDetails.as_view()),

    path('call_to_action', CallToActionList.as_view()),
    path('call_to_action/<int:pk>/', CallToActionDetails.as_view()),

    path('story_id', StoryIdList.as_view()),
    path('story_id/<int:pk>/', StoryIdDetails.as_view()),

    path('approval_name', ApprovalNameList.as_view()),
    path('aproval_name/<int:pk>/', ApprovalNameDetails.as_view()),

]