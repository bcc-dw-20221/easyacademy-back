from time import time
from django.shortcuts import HttpResponse
from .models import ClassHours, Sector
from django.core import serializers
from django.views.decorators.http import require_http_methods

'''
 EndPoints para entidade Sector
'''
@require_http_methods(["GET"])
def get_sectors(request):
   sectors=Sector.objets.all()
   
   resp_json = serializers.serialize('json', sectors)
   
   return HttpResponse(resp_json, "application/json")


@require_http_methods(["GET"])
def get_sector(request, id):
   sector=Sector.objets.filter(pk=id)
   
   resp_json = serializers.serialize('json', sector)
   
   return HttpResponse(resp_json, "application/json")


@require_http_methods(["POST"])
def post_sector(request):
    sector = Sector()
    sector.name=request.POST["name"]
    sector.save()
    
    return HttpResponse("Setor criado com sucesso")


@require_http_methods(["DELETE"])
def delete_sector(request, id):
   sector=Sector.objets.filter(pk=id)
   sector.delete()
   
   return HttpResponse("Setor deletado com sucesso")

'''
 EndPoints para entidade ClassHours
'''
@require_http_methods(["GET"])
def get_class_hours(request):
   class_time=Sector.objets.all()
   
   resp_json = serializers.serialize('json', class_time)
   
   return HttpResponse(resp_json, "application/json")


@require_http_methods(["GET"])
def get_class_hours(request, id):
   class_time=ClassHours.objets.filter(pk=id)
   
   resp_json = serializers.serialize('json', class_time)
   
   return HttpResponse(resp_json, "application/json")


@require_http_methods(["POST"])
def post_sectors(request):
    time = Sector()
    time.name=request.POST["day_week"]
    time.name=request.POST["time_class"]
    time.name=request.POST["class_shift"]
    time.save()
    
    return HttpResponse("Setor criado com sucesso")


@require_http_methods(["DELETE"])
def delete_sector(request, id):
   time=Sector.objets.filter(pk=id)
   time.delete()
   
   return HttpResponse("Setor deletado com sucesso")

