from django.db import models

# Create your models here.


class Product_Category(models.Model):
    PCID=models.IntegerField()
    PCName=models.CharField(max_length=100)
    
    def __str__(self):
        return self.PCName
    
    
class Product(models.Model):
    PCName=models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    PID=models.IntegerField()
    PName=models.CharField(max_length=100)
    Price=models.IntegerField()
    PDescription=models.CharField(max_length=100)
    Pdate=models.DateField()
    
    def __str__(self):
        return self.PName
    
    