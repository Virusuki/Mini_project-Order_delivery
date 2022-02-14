from email.policy import default
from django.db import models

# Create your models here.

class Shop(models.Model):
    shop_name = models.CharField(max_length=20)
    shop_address = models.CharField(max_length=40)
    
class Menu(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)
    
    
class Order(models.Model): # 특정 사용자가 주문한 내역
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    order_date = models.DateTimeField('date ordered')
    address = models.CharField(max_length=40)
    estimated_time = models.IntegerField(default=-1) # 사장님이 입력 전 기본 -1
    deliver_finish = models.BooleanField(default=0)
    
    
class Orderfood(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=20)
 
   

