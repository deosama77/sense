from django.db import models

class Campiagn(models.Model):
    code =models.CharField(max_length=150 , blank=True,null=True,unique=True)
    platform=models.CharField(max_length=120)
    placement=models.CharField(max_length=120)
    page_name=models.CharField(max_length=120)
    campaign_name = models.CharField(max_length=150)
    campaign_objective =models.CharField(max_length=120)
    retargeting =models.CharField(max_length=120 , blank=True , null=True)
    engagement =models.CharField(max_length=120 , blank=True , null=True)
    add_set_name =models.CharField(max_length=120)
    audience = models.CharField(max_length=120 , blank=True , null=True)
    excluded_custom =models.CharField(max_length=120 , blank=True , null=True)
    add_name=models.CharField(max_length=120)
    audience_interest=models.CharField(max_length=250 , blank=True , null=True)
    title=models.CharField(max_length=120 , blank=True , null=True)
    body = models.CharField(max_length=300 , blank=True , null=True)
    link_description = models.CharField(max_length=250 , blank=True , null=True)
    display_link = models.CharField(max_length=120 , blank=True , null=True)
    image_video_file_name = models.CharField(max_length=120 , blank=True , null=True)
    display_link = models.CharField(max_length=250 , blank=True , null=True)
    product_1_link = models.CharField(max_length=250 , blank=True , null=True)
    product_name = models.CharField(max_length=120 , blank=True , null=True)
    product_image_hash = models.CharField(max_length=120 , blank=True , null=True)
    call_to_action=models.CharField(max_length=120 , blank=True , null=True)
    store_id = models.CharField(max_length=120 , blank=True , null=True)
    approval_name= models.CharField(max_length=120 , blank=True , null=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.campaign_name


class Audience(models.Model):
    label=models.CharField(max_length=140)

    def __str__(self):
        return self.label

class Code(models.Model):
    label=models.CharField(max_length=140 , unique=True)

    def __str__(self):
        return self.label

class Platform(models.Model):
    label=models.CharField(max_length=140)

    def __str__(self):
        return self.label

class Placement(models.Model):
    label=models.CharField(max_length=140)

    def __str__(self):
        return self.label

class PageName(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_page_name"

    def __str__(self):
        return self.label

class CampaignName(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_campaign_name"

    def __str__(self):
        return self.label

class CampaignObjective(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_campaign_objective"

    def __str__(self):
        return self.label

class Retargeting(models.Model):
    label=models.CharField(max_length=140)

    def __str__(self):
        return self.label

class Engagement(models.Model):
    label=models.CharField(max_length=140)

    def __str__(self):
        return self.label

class AddSetName(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_add_set_name"
    def __str__(self):
        return self.label

class ExcludedCustom(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_excluded_custom"
    def __str__(self):
        return self.label


# other >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class CampaignStatus(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_campaign_status"
    def __str__(self):
        return self.label


class BuyingType(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_buying_type"
    def __str__(self):
        return self.label


class AdSetBidStrategy(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_ad_set_bid_strategy"
    def __str__(self):
        return self.label


class BillingEvent(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_billing_event"
    def __str__(self):
        return self.label


class OptimizationGoal(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_optimization_goal"
    def __str__(self):
        return self.label

class AudienceNetworkPositions(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_audience_network_positions"
    def __str__(self):
        return self.label


class MessengerPositions(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_messenger_positions"
    def __str__(self):
        return self.label

class FacebookPositions(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_facebook_positions"
    def __str__(self):
        return self.label

class InstagramPositions(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_instagram_positions"
    def __str__(self):
        return self.label

class AdSetRunStatus(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_ad_set_run_status"
    def __str__(self):
        return self.label

class CampaignBidStrategy(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_campaign_bid_strategy"
    def __str__(self):
        return self.label

class AdStatus(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_ad_status"
    def __str__(self):
        return self.label

class OculusPositions(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "api_oculus_positions"
    def __str__(self):
        return self.label