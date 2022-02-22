from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from order.models import Shop, Menu, Order, Orderfood
from order.serializers import ShopSerializer, MenuSerializer
from user.serializers import UserSerializer
from user.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

'''
@csrf_exempt
def shop(request):
    if request.method == 'GET':    
        user = User.objects.all()
        return render(request, 'order/shop_list.html', {'user_list':shop})
        

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShopSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
'''