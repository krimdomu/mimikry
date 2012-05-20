# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from opendcm.models.hardware import System as SystemModel

def index(request, system_id):
    system = SystemModel.objects.get(pk=system_id)    
    return render(request, 'kickstart.tpl', {'system': system}, content_type="text/plain")
