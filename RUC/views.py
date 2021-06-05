import RUC
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import RUC
from .serializers import RazonSocialSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def RUC_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        razSociales = RUC.objects.all()
        serializer = RazonSocialSerializer(razSociales, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RazonSocialSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)
@csrf_exempt
def RUC_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        razSocial = RUC.objects.get(rucEmpresa=pk)
    except RUC.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RazonSocialSerializer(razSocial)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RazonSocialSerializer(razSocial, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        RUC.delete()
        return HttpResponse(status=204)
@csrf_exempt
def RUC_DNI_detail(request, pk):
    """
    Retrieve, update or delete a serie.
    """
    try:
        razSocial = RUC.objects.get(identificacion=pk)
    except RUC.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = RazonSocialSerializer(razSocial)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RazonSocialSerializer(razSocial, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        RUC.delete()
        return HttpResponse(status=204)