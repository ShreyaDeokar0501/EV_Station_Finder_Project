from django.db import models

# Create your models here.

## User login
class newuser(models.Model):
    Username=models.CharField(max_length=80)
    fname=models.CharField(max_length=89)
    lname=models.CharField(max_length=88)
    email=models.EmailField(max_length=90)
    pass1=models.CharField(max_length=90)
    pass2=models.CharField(max_length=90)


## owner login
class Stationowner(models.Model):
    Username=models.CharField(max_length=80)
    fname=models.CharField(max_length=89)
    lname=models.CharField(max_length=88)
    email=models.EmailField(max_length=90)
    pass1=models.CharField(max_length=90)
    pass2=models.CharField(max_length=90)



class Stations(models.Model):
    sname=models.CharField(max_length=250)
    address= models.CharField(max_length=540)
    area=models.CharField(max_length=90,null='True')
    city=models.CharField(max_length=250)
    phone=models.CharField(max_length=340)
    ctslot=models.CharField(max_length=120)
    details=models.CharField(max_length=290,default='0')
    Location=models.CharField(max_length=290,default='0')


class Bookslots(models.Model):
    oname=models.CharField(max_length=250)
    vehicleno= models.CharField(max_length=540)
    mobileno=models.CharField(max_length=90,null='True')
    city=models.CharField(max_length=250)
    area=models.CharField(max_length=340)
    time=models.CharField(max_length=120)
    date=models.CharField(max_length=120,default='0')
    

class Payment(models.Model):
    hname=models.CharField(max_length=120,default='0')
    accountno=models.CharField(max_length=120,default='0')
    ifsccode=models.CharField(max_length=120,default='0')
    total=models.CharField(max_length=120,default='0')



class Review(models.Model):

    SEMESTER_CHOICES = (
        ("1", "Poor"),
        ("2", "Fair "),
        ("3", "Good "),
        ("4", "Very Good"),
        ("5", "Excellent"),
     
        )
    title=models.CharField(max_length=120,default='0')
    rating=models.CharField(max_length=20,choices = SEMESTER_CHOICES,default='0')
    comment=models.CharField(max_length=120,default='0')
    