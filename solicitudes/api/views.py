from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Solicitud
from .serializers import SolicitudSerializer


class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all().order_by('-id')
    serializer_class = SolicitudSerializer
