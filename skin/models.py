from django.db import models

# Create your models here.
class imagee(models.Model):
    image=models.ImageField(upload_to="image")

class patreg(models.Model):
    uname=models.CharField(max_length=50)
    passw=models.CharField(max_length=50)
    contact=models.CharField(max_length=50)
    email=models.EmailField()
    address=models.TextField()



    