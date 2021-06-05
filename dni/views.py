from re import T
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import DNI
from .serializers import DNISerializer

class JSONResponse(HttpResponse):
    def __init__(self,data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def dni_list(request):

    if request.method == 'GET':
        dni = DNI.objects.all()
        serializer =DNISerializer(dni, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DNISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data ,status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def dni_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        dni = DNI.objects.get(dni=pk)
    except DNI.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = DNISerializer(dni)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = DNISerializer(dni, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        dni.delete()
        return HttpResponse(status=204)
