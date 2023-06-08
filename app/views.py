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
    
    
    
        