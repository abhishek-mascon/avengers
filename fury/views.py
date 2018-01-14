# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.core import serializers
from fury.models import Portfolio, Stocks
import json

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def test(request, format=None):
    content = {
        'status': 'request was permitted'
    }
    return Response(content)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_portfolio(request):
    user = request.user
    user_id = user.id
    portfolio = Portfolio.objects.filter(user_id=user_id)
    content = serializers.serialize("json", portfolio)
    return Response(json.loads(content))


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def get_stock_codes(request):
    stock_codes = Stocks.objects.values('id', 'symbol')
    return Response(stock_codes)
    

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def add_to_portfolio(request):
    content = {
        'status': 'Portfolio updated'
    }
    try:
        user = request.user
        body = json.loads(request.body)
        items = body['items']
        for item in items:
            stock = item['stock']['label']
            shares = item['shares']
            notes = item['notes']
            price = item['price']
            p = Portfolio(user = user, stock = stock, shares = shares, notes = notes, price = price)
            p.save()
        return Response(content, status=status.HTTP_200_OK)
    except Exception as e:
        content['status'] = "Failed with " + str(e)
    return Response(content, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    



