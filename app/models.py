from django.db import models

# Create your models here.
class Student(models.Model):
    studentNo=models.CharField(max_length=20,unique=True,verbose_name='Ma')
    name=models.CharField(max_length=50,verbose_name='Ten')
    address=models.CharField(max_length=200,blank=True,verbose_name='Dia chi')
