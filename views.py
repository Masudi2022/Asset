from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import *
from . models import *
# Create your views here.

@api_view(['GET'])
def office(request):
    if request.method == 'GET':
        office = Office.objects.all()
        serializer = OfficeSerlializer(office, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def division(request):
    if request.method == 'GET':
        division = Division.objects.all()
        serializer = DivisionSerializer(division, many=True)
        return Response(serializer.data)
    

@api_view(['GET'])
def asset(request):
    if request.method == 'GET':
        asset = Asset.objects.all()
        serializer = AssetSerializer(asset, many=True)
        return Response(serializer.data)


