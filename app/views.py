from django.shortcuts import render
from app.serializers import *
from rest_framework.response import Response
from app.models import *
from rest_framework.views import APIView


# Create your views here.
class ProductCrud(APIView):
    def get(self,request):
        PQS=product.objects.all()
        PJD=ProductMS(PQS,many=True)
        return Response(PJD.data)
    def post(self,request):
        PMSD=ProductMS(data=request.data)
        if PMSD.is_valid():
            SPO=PMSD.save()
            return Response({'message':'product is created'})
        else:
            return Response({'message':'product creation is failed'})
    def put(self,request):
        Pid=request.data['Pid']
        PO=product.objects.get(Pid=Pid)
        UPO=ProductMS(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':'product is updated'})
        else:
            return Response({'message':'product creation is updated'})




