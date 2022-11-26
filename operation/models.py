from django.db import models

class AddName(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "operation_add_name"

    def __str__(self):
        return self.label

class AudienceInterest(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "operation_audience_interest"

    def __str__(self):
        return self.label

class Title(models.Model):
    label=models.CharField(max_length=140)

    def __str__(self):
        return self.label

class Body(models.Model):
    label=models.CharField(max_length=140)

    def __str__(self):
        return self.label

class FileName(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "file_name"

    def __str__(self):
        return self.label

class ProductName(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "operation_product_name"

    def __str__(self):
        return self.label

class ProductImageHash(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "operation_product_image_hash"

    def __str__(self):
        return self.label

class CallToAction(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "operation_call_to_action"

    def __str__(self):
        return self.label

class StoryId(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "operation_story_id"

    def __str__(self):
        return self.label

class ApprovalName(models.Model):
    label=models.CharField(max_length=140)
    class Meta:
        db_table = "operation_approval_name"

    def __str__(self):
        return self.label
