from django.template import Context, loader
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required

#internal imports
from opendcm.models.hardware import System

@login_required(login_url='/auth/login/')
def index(request):
    systems = System.objects.all()
    return render_to_response('opendcm/index.html', {'object_list': systems},
        context_instance=RequestContext(request))

@login_required(login_url='/auth/login/')
def detail(request, name):
    system = get_object_or_404(System, name=name)
    return render_to_response('opendcm/system.html', {'object': system},
        context_instance=RequestContext(request))
