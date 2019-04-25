from django.shortcuts import render

from rest_framework import views
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def Return200Ok(request, **kwargs):
    return Response(data="", status=200)
