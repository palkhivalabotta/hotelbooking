from django.db import models



class availablerooms(models.Model):
    idno=models.IntegerField(primary_key=True)
    room_type=models.CharField(max_length=25)
class amount(models.Model):
    idno = models.ForeignKey(availablerooms,on_delete=models.CASCADE)
    cost=models.IntegerField()
class UserRegister(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email_id = models.EmailField(max_length=20, primary_key=True)
    password = models.CharField(max_length=50)
    rpassword = models.CharField(max_length=50)
    contact_no = models.IntegerField()
    address = models.CharField(max_length=100)
class Contact(models.Model):
    name=models.CharField(max_length=20)
    Email_id=models.EmailField(max_length=20)
    phone_no=models.IntegerField()
    message=models.CharField(max_length=220)
class book(models.Model):
    rom=models.CharField(max_length=50)
    paru=models.CharField(max_length=50)
    cin=models.DateField()
    cout=models.DateField()
    cno=models.IntegerField()
    addr=models.CharField(max_length=250)
    cnum=models.IntegerField()
    cv = models.IntegerField()
    cord_type = models.CharField(max_length=20)
class card(models.Model):
    idno = models.IntegerField(primary_key=True)
    card_type = models.CharField(max_length=25)
