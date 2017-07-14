from datetime import datetime

from django.db import connection

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer    

from rest_framework.views import APIView

# TODO TEMPLATE-USER: implement serializers
# from .serializers import <...>

def index(request):
    return JsonResponse(dict(success=True), safe=False)
    
# TODO TEMPLATE-USER: implement your REST API