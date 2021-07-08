from rest.serializer import ObraSerializer
from django.views.decorators.csrf import csrf_exempt
from rest.serializer import ObraSerializer
from django.shortcuts import render
from core.models import Arte
from rest_framework.response import Response
from rest_framework.decorators import api_view

#Get: listar todas las obras
@csrf_exempt
@api_view(['GET'])

def lista_Obras(request):
    if request.method == 'GET':
        Artes = Arte.objects.all()
        serializer = ObraSerializer(Artes,many=True)
        return Response(serializer.data)
