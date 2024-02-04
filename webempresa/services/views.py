from django.shortcuts import render
from .models import Service

def service(request):
    services  = Service.objects.all()

    return render(request, "services/services.html", {'services': services})