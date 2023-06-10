from django.db import models

# Create your models here.
class product_category(models.Model):
    PCid=models.IntegerField(primary_key=True)
    PCname=models.CharField(max_length=100)

    def __str__(self):
       return self.PCname


class product(models.Model):
    PCname=models.ForeignKey(product_category,on_delete=models.CASCADE)
    Pid=models.IntegerField(primary_key=True)
    Pname=models.CharField(max_length=100)
    Pprice=models.DecimalField(decimal_places=2,max_digits=8)
    Pdescription=models.CharField(max_length=100)
    Pdate=models.DateField()

    def __str__(self):
       return self.Pname

