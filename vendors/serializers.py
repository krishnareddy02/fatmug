from rest_framework import serializers
from .models import *

class vender_data2_serializer2(serializers.ModelSerializer):
    class Meta:
        model=vender_data2
        fields=['issue_date','acknoweldgement_date']

class vender_data2_serializer3(serializers.ModelSerializer):
    class Meta:
        model=vender_data2
        fields=['name','venders_code','order_date','delivery_date','successful_deliverd_date','status','issue_date','acknoweldgement_date']

class vender_data21_serializer(serializers.ModelSerializer):
    class Meta:
        model=vender_data21
        fields='__all__'   

class vender_data2_serializer(serializers.ModelSerializer):
    class Meta:
        model=vender_data2
        fields=['contact_details']

class vender_code_serializer(serializers.ModelSerializer):
    class Meta:
        model=vender_details
        fields='__all__'

