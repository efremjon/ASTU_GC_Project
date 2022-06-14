from django.db import models
from Agent.models import Customer,Product_in_Agent_Stor
from Company.models import Product

# Create your models here.


class Customer_order(models.Model):
  STATUS = (
      ('Pending', 'Pending'),
      ('Not Recived', 'Not Recived'),
      ('Delivered', 'Delivered'),
      ) 
  Driver = (
      ('Assigned', 'Assigned'),
      ('Not Assigned', 'Not Assigned'),
      ) 
  Customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  driver = models.CharField(max_length=200, null=True, choices=Driver)
  status = models.CharField(max_length=200, null=True, choices=STATUS, default='Not Assigned')
  def __str__(self) -> str:
      return str(self.Customer) + " |" + " Order " + str(self.id)
      
products=Product.objects.all()
for product in products:
    Customer_order.add_to_class(product.Product_Name,models.IntegerField(default=0,null=True,blank=True))  

class Customer_Transaction(models.Model):
  Paid_status = (
      ('Paid', 'Paid'),
      ('Not Paid', 'Not Paid'),
      ) 
  Customer_order_id=models.OneToOneField(Customer_order, on_delete=models.CASCADE,null=True)
  date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  Total_Amount = models.FloatField(default=0.0,null=True,blank=True) 
  Paid_status = models.CharField(max_length=200, null=True, choices=Paid_status)
  TransactionCode = models.CharField(max_length=200,null=True)
  MarchentId = models.CharField(max_length=200, null=True, )
  def __str__(self) -> str:
      return str(self.TransactionCode)
# 

