from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

class FirstApiView(APIView):
    def get(self, request):
        return Response(data={'message:' 'Hello World'})
