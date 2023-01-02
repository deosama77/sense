from rest_framework import generics
from .serializers import CampiagnSerializer,AudienceSerializer,AddSetNameSerializer,PlatformSerializer,PlacementSerializer,CampaignNameSerializer\
    ,PageNameSerializer,CampaignObjectiveSerializer,ExcludedCustomSerializer,CodeSerializer,EngagementSerializer,RetargetingSerializer
from .models import Campiagn,Audience,AddSetName,Platform,Placement,CampaignName,PageName,CampaignObjective,ExcludedCustom,Code,Engagement,Retargeting
from django.http import  FileResponse  , HttpResponse

# other
from .models import CampaignBidStrategy,AdSetRunStatus,InstagramPositions,FacebookPositions,MessengerPositions,AudienceNetworkPositions,OptimizationGoal,BillingEvent,AdSetBidStrategy,BuyingType,CampaignStatus , AdStatus ,OculusPositions
from .serializers import CampaignBidStrategySerializer,AdSetRunStatusSerializer ,InstagramPositionsSerializer , FacebookPositionsSerializer , MessengerPositionsSerializer,AudienceNetworkPositionsSerializer,OptimizationGoalSerializer,BillingEventSerializer,AdSetBidStrategySerializer,BuyingTypeSerializer,CampaignStatusSerializer , AdStatusSerializer, OculusPositionsSerializer

from io import BytesIO
import os
import pandas as pd


def export_to_excel(request):
    path_static_excel=os.path.abspath(os.path.dirname(__file__))+"/"+"excel"+"/"+"AdsManagerTemplate.xltx"
    # path_static_excel="/static/excel/"+"AdsManagerTemplate.xltx"
    df2=pd.read_excel(path_static_excel)
    data = []
    objs=Campiagn.objects.all();
    for obj in objs:
        columnData = {}
        for name, sheet in df2.items():
            if (name == "Campaign Name"):
                columnData[name] = getValueByField(obj,'campaign_name')
            elif(name=='Campaign Objective'):
                columnData[name] = getValueByField(obj,'campaign_objective')
            elif(name=="Ad Set Name"):
                columnData[name] = getValueByField(obj,'add_set_name')
            elif (name == "Ad Name"):
                columnData[name] = getValueByField(obj, 'add_name')
            elif (name == "title"):
                columnData[name] = getValueByField(obj, 'title')
            elif (name == "body"):
                columnData[name] = getValueByField(obj, 'body')
            elif (name == "Link Description"):
                print("Link discription" , getValueByField(obj, 'link_description'))
                columnData[name] = getValueByField(obj, 'link_description')
            elif (name == "Display Link"):
                columnData[name] = getValueByField(obj, 'display_link')
            elif (name == "Product 1 - Link"):
                print("Product 1-Link", getValueByField(obj, 'product_1_link'))
                columnData[name] = getValueByField(obj, 'product_1_link')
            elif (name == "Story ID"):
                columnData[name] = getValueByField(obj, 'store_id')
            elif (name == "Call to Action"):
                columnData[name] = getValueByField(obj, 'call_to_action')
            elif (name == "Image File Name"):
                columnData[name] = getValueByField(obj, 'image_video_file_name')
            elif (name == "Product 1 - Name"):
                columnData[name] = getValueByField(obj, 'product_name')
            elif (name == "Product 1 - Image Hash"):
                columnData[name] = getValueByField(obj, 'product_image_hash')
            else:
                columnData[name] = ""
        data.append(columnData)

    with BytesIO() as b:
        with pd.ExcelWriter(b) as writer:
            # You can add multiple Dataframes to an excel file
            # Using the sheet_name attribute
            pd.DataFrame(data).to_excel(writer,sheet_name="DATA 1",index=False)

        filename = "AdsManager.xlsx"

        res = HttpResponse(
            b.getvalue(),  # Gives the Byte string of the Byte Buffer object
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        res['Content-Disposition'] = f'attachment; filename={filename}'
        return res

    return FileResponse(df)

def getValueByField(obj,fieldName):
    field_object = obj._meta.get_field(fieldName)
    field_value = field_object.value_from_object(obj)
    return field_value;


class CampiagnList(generics.ListCreateAPIView):
    serializer_class=CampiagnSerializer

    def get_queryset(self):
        queryset=Campiagn.objects.all()
        Audience=self.request.query_params.get('customAudience')
        if Audience is not None:
            queryset.filter(customAudience=Audience)
        return queryset

class CampiagnDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Campiagn.objects.all()
    serializer_class = CampiagnSerializer

class AudienceList(generics.ListCreateAPIView):
    serializer_class = AudienceSerializer
    queryset = Audience.objects.all()

class AudienceDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AudienceSerializer
    queryset = Audience.objects.all()


class AddSetNameList(generics.ListCreateAPIView):
    serializer_class = AddSetNameSerializer
    queryset = AddSetName.objects.all()

class AddSetNameDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddSetNameSerializer
    queryset = AddSetName.objects.all()

class PlatformList(generics.ListCreateAPIView):
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()

class PlatformDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlatformSerializer
    queryset = Platform.objects.all()

class PlacementList(generics.ListCreateAPIView):
    serializer_class = PlacementSerializer
    queryset = Placement.objects.all()

class PlacementDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PlacementSerializer
    queryset = Placement.objects.all()

class CampaignNameList(generics.ListCreateAPIView):
    serializer_class = CampaignNameSerializer
    queryset = CampaignName.objects.all()

class CampaignNameDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CampaignNameSerializer
    queryset = CampaignName.objects.all()

class PageNameList(generics.ListCreateAPIView):
    serializer_class = PageNameSerializer
    queryset = PageName.objects.all()

class PageNameDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PageNameSerializer
    queryset = PageName.objects.all()

class CampaignObjectiveList(generics.ListCreateAPIView):
    serializer_class = CampaignObjectiveSerializer
    queryset = CampaignObjective.objects.all()

class CampaignObjectiveDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CampaignObjectiveSerializer
    queryset = CampaignObjective.objects.all()

class CodeList(generics.ListCreateAPIView):
    serializer_class = CodeSerializer
    queryset = Code.objects.all()

class CodeDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CodeSerializer
    queryset = Code.objects.all()

class ExcludedCustomList(generics.ListCreateAPIView):
    serializer_class = ExcludedCustomSerializer
    queryset = ExcludedCustom.objects.all()

class ExcludedCustomDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExcludedCustomSerializer
    queryset = ExcludedCustom.objects.all()

class EngamentList(generics.ListCreateAPIView):
    serializer_class = EngagementSerializer
    queryset = Engagement.objects.all()

class EngamentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EngagementSerializer
    queryset = Engagement.objects.all()

class RetargetingList(generics.ListCreateAPIView):
    serializer_class = RetargetingSerializer
    queryset = Retargeting.objects.all()

class RetargetingDetails(generics.RetrieveUpdateDestroyAPIView):
    erializer_class = RetargetingSerializer
    queryset = Retargeting.objects.all()


# Other views ..............................................
class CampaignStatusList(generics.ListCreateAPIView):
    serializer_class = CampaignStatusSerializer
    queryset = CampaignStatus.objects.all()

class CampaignStatusDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CampaignStatusSerializer
    queryset = CampaignStatus.objects.all()

class AdSetRunStatusList(generics.ListCreateAPIView):
    serializer_class = AdSetRunStatusSerializer;
    queryset = AdSetRunStatus.objects.all()

class AdSetRunStatusDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdSetRunStatusSerializer;
    queryset = AdSetRunStatus.objects.all()

class CampaignBidStrategyList(generics.ListCreateAPIView):
    serializer_class = CampaignBidStrategySerializer
    queryset = CampaignBidStrategy.objects.all()

class CampaignBidStrategyDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CampaignBidStrategySerializer
    queryset = CampaignBidStrategy.objects.all()

class InstagramPositionsList(generics.ListCreateAPIView):
    serializer_class = InstagramPositionsSerializer
    queryset = InstagramPositions.objects.all()

class InstagramPositionsDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = InstagramPositionsSerializer
    queryset = InstagramPositions.objects.all()

class FacebookPositionsList(generics.ListCreateAPIView):
    serializer_class = FacebookPositionsSerializer
    queryset = FacebookPositions.objects.all()

class FacebookPositionsDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FacebookPositionsSerializer
    queryset = FacebookPositions.objects.all()

class MessengerPositionsList(generics.ListCreateAPIView):
    serializer_class = MessengerPositionsSerializer
    queryset = MessengerPositions.objects.all()

class MessengerPositionsDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessengerPositionsSerializer
    queryset = MessengerPositions.objects.all()

class AudienceNetworkPositionsList(generics.ListCreateAPIView):
    serializer_class = AudienceNetworkPositionsSerializer
    queryset = AudienceNetworkPositions.objects.all()

class AudienceNetworkPositionsDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AudienceNetworkPositionsSerializer
    queryset = AudienceNetworkPositions.objects.all()

class OptimizationGoalList(generics.ListCreateAPIView):
    serializer_class = OptimizationGoalSerializer
    queryset = OptimizationGoal.objects.all()

class OptimizationGoalDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OptimizationGoalSerializer
    queryset = OptimizationGoal.objects.all()

class BillingEventList(generics.ListCreateAPIView):
    serializer_class = BillingEventSerializer
    queryset = BillingEvent.objects.all()

class BillingEventDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BillingEventSerializer
    queryset = BillingEvent.objects.all()

class AdSetBidStrategyList(generics.ListCreateAPIView):
    serializer_class = AdSetBidStrategySerializer
    queryset = AdSetBidStrategy.objects.all()

class AdSetBidStrategyDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdSetBidStrategySerializer
    queryset = AdSetBidStrategy.objects.all()

class BuyingTypeList(generics.ListCreateAPIView):
    serializer_class = BuyingTypeSerializer
    queryset = BuyingType.objects.all()

class BuyingTypeDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BuyingTypeSerializer
    queryset = BuyingType.objects.all()


class AdStatusList(generics.ListCreateAPIView):
    serializer_class = AdStatusSerializer
    queryset = AdStatus.objects.all()

class AdStatusDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AdStatusSerializer
    queryset = AdStatus.objects.all()

class OculusPositionsList(generics.ListCreateAPIView):
    serializer_class = OculusPositionsSerializer
    queryset = OculusPositions.objects.all()

class OculusPositionsDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OculusPositionsSerializer
    queryset = OculusPositions.objects.all()
