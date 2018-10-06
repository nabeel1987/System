from django.db import models
from django.apps import apps
from Customer.models import Profile
from Inventory.models import *
from Employee.models import *

# Create your models here.
class NewOrder(models.Model):
    OrderName=models.CharField(max_length=200) #    OrderId = models.AutoField(primary_key=True)
    Inventory = models.ForeignKey(Items, related_name='display_category',on_delete=models.CASCADE)
    #Brand=models.ForeignKey(Brand,related_name='Brands',on_delete=models.CASCADE)

    Customer=models.ForeignKey(Profile,on_delete=models.CASCADE)
    Employee=models.ForeignKey(EmployeeProfile,on_delete=models.CASCADE)
#    Price=Inventory.display_category
    #Price=models.ForeignKey(SellPrice,related_name="PRICE",on_delete=models.CASCADE)

    #Price=Laptop.objects.get(pk=1)


    def __str__(self):

        return 'OrderName={0}, Price={1}'.format(self.OrderName, self.Inventory.SellPrice)
