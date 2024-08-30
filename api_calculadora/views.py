import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

# Create your views here.
class SumaView(APIView):
    def get(self, request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        suma=int(num_uno)+ int(num_dos)
        return Response(suma, status.HTTP_200_OK)

class RestaView(APIView):
    def get(self, request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        resta=int(num_uno)- int(num_dos)
        return Response(resta, status.HTTP_200_OK)
    
class MultiplicacionView(APIView):
    def get(self, request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        multiplicacion=int(num_uno)* int(num_dos)
        return Response(multiplicacion, status.HTTP_200_OK)

class DivisionView(APIView):
    def get(self, request, *args, **kwargs):
        num_uno=request.GET.get('num_uno')
        num_dos=request.GET.get('num_dos')
        division=int(num_uno)/ int(num_dos)
        return Response(division, status.HTTP_200_OK)
