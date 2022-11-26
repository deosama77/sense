from rest_framework import generics
from .serializers import CampiagnSerializer,AudienceSerializer,AddSetNameSerializer,PlatformSerializer,PlacementSerializer,CampaignNameSerializer\
    ,PageNameSerializer,CampaignObjectiveSerializer,ExcludedCustomSerializer,CodeSerializer,EngagementSerializer,RetargetingSerializer
from .models import Campiagn,Audience,AddSetName,Platform,Placement,CampaignName,PageName,CampaignObjective,ExcludedCustom,Code,Engagement,Retargeting
from django.http import  FileResponse , JsonResponse , HttpResponse

import io
from io import BytesIO
import os
import pandas as pd


def export_to_excel(request):
    # path_excel=os.path.abspath(os.path.dirname(__file__))+"\\"+"excel"+"\\"+"AdsManagerTemplate.xltx"
    path_static_excel=path_excel="static/excel/"+"AdsManagerTemplate.xltx"
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
# def campaign_excel(request):
#   campaigns = Campiagn.objects.all()
#   buffer = io.BytesIO()
#   workbook = xlsxwriter.Workbook(buffer)
#   worksheet = workbook.add_worksheet("Ads Manager Template")
#   header=['Campaign ID', 'Campaign Name','Campaign Status','Special Ad Categories','Special Ad Category Country',
#                                          'Campaign Objective','Buying Type','Campaign Spent Limit','Campaign Daily Budget',
#                                          'Campaign Lifetime Budget','Campaign Bid Strategy','Tags','Campaign Is Using L3 Schedule',
#                                          'Campaign Start Time','Campaign Stop Time' , 'Ad Set ID' ,'Ad Set' ,'Run Status' ,'Ad Set Name' , 'Ad Set Time Start'
#                                           'Ad Set Time Stop' ,'Ad Set Daily Budget' ,'Ad Set Lifetime Budget' ,'Link Object ID' ,'Link Application ID',
#                                          'Countries', 'Global Regions', 'Excluded Global Regions', 'Cities', 'Regions',
#                                          'Zip', 'Gender', 'Age Min', 'Age Max', 'Education Status',
#                                          'College Start Year', 'College End Year','Interested In','Relationship','Connections','Excluded Connections','Friends of Connections'
#                                          ,"Locles","Broad Category Clusters","Custom Audiences"
#                                           ,"Excluded Custom Audiences","Location Cluster IDs","Publisher Platforms" ,"Device Platforms","Facebook Positions"
#           "Excluded Location Cluster IDs",]
#
#   print("Abso path",os.path.abspath(os.path.dirname(__file__))+"\\"+"excel"+"\\"+"AdsManagerTemplate.xltx")
#
#   campaigns_list = campaigns.values_list('platform','placement')
#
#   for idx, month in enumerate(header):
#       worksheet.write(0, idx, header[idx])
#   for rowid in range(len(campaigns_list)):
#       for columnid in range(len(campaigns_list[rowid])):
#         worksheet.write(rowid+1, columnid, campaigns_list[rowid][columnid])
#
#   workbook.close()
#   buffer.seek(0)
#   headers = {'Content-Disposition': 'attachment; filename="campaign.xlsx"'}
#   return FileResponse(buffer, headers=headers)

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




