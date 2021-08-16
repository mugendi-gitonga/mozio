from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from core.models import *
from .utils import check_if_in_polygon

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['GET'])
def get_providers(request):

    endpoints = {
        'Get Providers': '/get_all_providers/',
        'Provider details': '/provider_details/',
        'Create Provider': '/create_provider/',
        'Update Providers': '/update_provider/',
        'Delete Provider': '/delete_provider/',
        'Create Polygon':'/create_polygon/',
        'Update Polygon':'/update_polygon/',
        'Delete Polygon': '/delet_polygon/',
        'Get nearest provider': '/nearest_providers'
    }

    return Response(endpoints)


@api_view(['POST', 'GET'])
def nearest_providers(request, lat, lon):
    
    lattitude = int(lat)
    longitude = int(lon)
    point = ([lattitude, longitude])
    covered_areas = check_if_in_polygon(point)
    serializer = PolygonSerializer(covered_areas, many=True)

    return Response(serializer.data)



@api_view(['GET'])
def get_all_providers(request):
    
    providers = Provider.objects.all()
    serializer = ProviderSerializer(providers, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def provider_details(request, provider_id):
    
    provider = get_object_or_404(Provider, id=provider_id)
    serializer = ProviderSerializer(provider, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def create_provider(request):
    
    serializer = ProviderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        message = {
            'message':'provider added successfully'
        }
    else:
        message = {
            'message':'please try again'
        }
        

    return Response(message)


@api_view(['GET'])
def get_all_polygons(request, provider):
    
    polygons = Polygon.objects.filter(polygon_provider=provider)
    serializer = PolygonSerializer(polygons, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def create_polygon(request, provider):

    serializer = PolygonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        message = {
            'message':'polygon created successfully'
        }
    else:
        message = {
            'message':'please try again'
        }
        

    return Response(message)


@api_view(['POST'])
def update_polygon(request, polygon):

    polygon = get_object_or_404(Polygon, id=polygon)
    serializer = PolygonSerializer(instance=polygon, data=request.data)
    if serializer.is_valid():
        serializer.save()

        message = {
            'message':'polygon updated successfully'
        }
    else:
        message = {
            'message':'please try again'
        }
        

    return Response(message)


@api_view(['DELETE'])
def delete_polygon(request, polygon):

    polygon = get_object_or_404(Polygon, id=polygon)
    polygon.delete()
    
    message = {
            'message':'polygon deleted successfully'
        }
        

    return Response(message)

