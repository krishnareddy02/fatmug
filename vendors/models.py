from django.db import models

# Create your models here.

class vender_details(models.Model):
    name=models.CharField(max_length=100)
    contact_details=models.IntegerField()
    address=models.TextField()
    venders_code=models.CharField(max_length=100)

class vender_data2(models.Model):
    name=models.CharField(max_length=100)
    contact_details=models.IntegerField()
    address=models.TextField()
    venders_code=models.CharField(max_length=100)
    order_date=models.DateTimeField()
    delivery_date=models.DateTimeField()
    successful_deliverd_date=models.DateTimeField()
    items=models.CharField(max_length=1000)
    quantity=models.IntegerField()
    status=models.CharField(max_length=100)
    issue_date=models.DateTimeField()
    acknoweldgement_date=models.DateTimeField()

class vender_data21(models.Model):
    po_number=models.CharField(max_length=100)
    venders_code=models.CharField(max_length=100)
    order_date=models.DateTimeField()
    delivery_date=models.DateTimeField()
    successful_deliverd_date=models.DateTimeField()
    status=models.CharField(max_length=100)
    issue_date=models.DateTimeField()
    acknoweldgement_date=models.DateTimeField()
    quality_rating=models.FloatField()
