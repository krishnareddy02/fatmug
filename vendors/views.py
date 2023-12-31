from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from datetime import datetime


# Create your views here.

def index(request):
    return render(request,'index.html')

def home_page(request):
    return render(request,'home.html')

def vender_page(request):
    return render(request,'vender.html')

def purchase_order(request):
    return render(request,'purchase_order.html')

def fulfillment_rate(request):
    if request.method=='POST':
        venders_code12=request.POST['venders_code']
        obj=vender_data2.objects.filter(venders_code=venders_code12)
        objs=vender_data2.objects.filter(venders_code=venders_code12).count()
        obj1=vender_data2.objects.filter(venders_code=venders_code12,status="completed").count()
        on_time_deliveries = vender_data2.objects.filter(successful_deliverd_date__lte=models.F('delivery_date'),venders_code=venders_code12).count()
        # otr=on_time_deliveries/obj1
        # on_time_delivery_rate=round(otr,2)*100
        serializer1=vender_data2_serializer2(obj,many=True)
        serializer=vender_data2_serializer(obj,many=True)
        rating=0
        for i in serializer.data:
            rating+=i['contact_details']
        if obj1==0:
            quality_rating_avg=0
        else:
            quality_rating_avg=rating/obj1
        if obj1==0:
            on_time_delivery_rate=0
        else:
            otr=on_time_deliveries/obj1
            on_time_delivery_rate=round(otr,2)*100
        time_differences=0
        for i in serializer1.data:
            time_differences+=(datetime.strptime(i['acknoweldgement_date'],"%Y-%m-%dT%H:%M:%SZ")-datetime.strptime(i['issue_date'],"%Y-%m-%dT%H:%M:%SZ")).days
        d1={
            "quality_rating_avg":quality_rating_avg,
            "otr":on_time_delivery_rate,
            "time_differences":time_differences
        }
        return render(request,'vender.html',context=d1)
    
def delete1(request,id):
    user=vender_details.objects.get(id=id)
    user.delete()
    return HttpResponse("THE VENDER DATA DELETED")

def delete(request,id):
    user=vender_data21.objects.get(id=id)
    user.delete()
    return HttpResponse("THE PURCHASE ORDER DATA DELETED")
    # user=vender_details.objects.get(id=id)
    # user.update()

@api_view(['POST','GET'])
def purchase_order_details(request):
    if request.method=='POST':
        data=request.data
        serializer=vender_data21_serializer(data=data)
        if serializer.is_valid():
            vd=vender_data21(
                            po_number=serializer.data['status'], 
                            status=serializer.data['status'],
                            quality_rating=serializer.data['quality_rating'],
                            # address=serializer1.data['address'],
                            venders_code=serializer.data['venders_code'],
                            order_date=serializer.data['order_date'],
                            delivery_date=serializer.data['delivery_date'],
                            successful_deliverd_date=serializer.data['successful_deliverd_date'],
                            # quantity=serializer1.data['quantity'],
                            # quality_rating_avg=serializer1.data['quality_rating'],
                            # average_response_time=serializer1.data['quantity'],                        # vendor=serializer1.data,
                            # items=serializer1.data['items'],
                            issue_date=serializer.data['issue_date'],
                            # on_time_delivery_rate=serializer1.data['quantity'],
                            # fulfillment_rate=serializer1.data['quantity']
                            acknoweldgement_date=serializer.data['acknoweldgement_date']
                            )
            vd.save()
            return render(request,'purchase_order.html')
        return Response(serializer.errors)
    
    if request.method=='GET':
        obj=vender_data21.objects.all()
        serializer=vender_data21_serializer(obj,many=True)
        data={
            "serializer":serializer.data
        }
        return render(request,'purchase_order_details.html',context=data)
@api_view(['GET','POST'])
def vender_data(request):
    if request.method=='POST':
        data=request.data
        serializer=vender_code_serializer(data=data)
        if serializer.is_valid():
            vd=vender_details(
                            name=serializer.data['name'],
                            contact_details=serializer.data['contact_details'],
                            address=serializer.data['address'],
                            venders_code=serializer.data['venders_code']
                            )
            vd.save()
            return render(request,'home.html')
        
    if request.method=='GET':
        obj=vender_details.objects.all()
        serializer=vender_code_serializer(obj,many=True)
        data={
            "serializer":serializer.data
        }
        return render(request,'venders.html',context=data)

