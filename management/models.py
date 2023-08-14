from django.db import models

# Create your models here.


class CustomerRecord(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone=models.CharField(max_length=15)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    zipcode=models.CharField(max_length=30)
    order_count=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return (f"{self.first_name} {self.last_name}")



