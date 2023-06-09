from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from rest_framework.decorators import permission_classes,api_view

from rest_framework.permissions import IsAuthenticated

from app.models import *

from app.serializer import *

from rest_framework.response import Response

@permission_classes([IsAuthenticated])
class Product_Curd(APIView):
    def get(self,request):
        SQS=Product.objects.all()
        PJD=ProductSerializer(SQS,many=True)
        return Response(PJD.data)
    
    def post(self,request):
        PMSD=ProductSerializer(data=request.data)### collect the date into models and giving into model seralizer and convert data
        if PMSD.is_valid():# is_valid is valid the data whatever the data will approprate giving or not
            PMSD.save()
            return Response({'message':'product is created:'})
        return Response({'Failed':'product is failed'})
    
    def put(self,request):
        # PID=request.get['PID']
        # UO=Product.objects.get(PID=PID)############ we have to write on based on object we have update the date
        id=request.data['id']
        UO=Product.objects.get(id=id)
        PUOD=ProductSerializer(UO,data=request.data)
        if PUOD.is_valid():
            PUOD.save()
            return Response({'message':'product is Update'})
        return Response({'Failed':'product is not Update'})
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        