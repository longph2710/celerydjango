from django.shortcuts import render
# framework
from rest_framework.decorators import api_view
from rest_framework.response import Response
# app
from . import tasks

# Create your views here.

@api_view(['GET'])
def add_number(request):
    x = int(request.GET['x'])
    y = int(request.GET['y'])
    result = tasks.add.delay(x, y)
    # print(result)
    return Response({"sum" : "ok"})

@api_view(['GET'])
def mul_number(request):
    x = int(request.GET['x'])
    y = int(request.GET['y'])
    result = tasks.mul.delay(x, y)
    # print(result)
    return Response({"sum" : "ok"})

@api_view(['GET'])
def perform_backup(request):
    database_id = request.GET['database_id']
    url = "http://127.0.0.1:8000/api/backup/history"
    tasks.perform_backup.delay(database_id, url)
    return Response({"message":"received"})