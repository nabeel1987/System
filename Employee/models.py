from django.db import models
from django.utils import timezone
from datetime import datetime
from django.db.models import CharField, Value as V
from django.db.models.functions import Concat



from django.contrib.auth.models import User
# Create your models here.
class EmployeeProfile(models.Model):
    user=models.OneToOneField(User,on_delete="models.CASCADE")
    designation=models.CharField(max_length=250,null=False,blank=False)
    salary=models.IntegerField(null=False,blank=False)
    working_days=models.IntegerField()
    pub_date = models.DateTimeField('Joining Date',default=datetime.now,null=True,blank=True)
    CURRENCY_CHOICES=(
        ('PKR','PKR'),
        ('EUR','EUR'),
        ('USD','USD'),
    )
    Currency=models.CharField(max_length=100,choices=CURRENCY_CHOICES)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


    def __str__(self):
        return str(self.user) #user is non-string, that why use str for integer
