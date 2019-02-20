from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(models.Model):
    username    = models.CharField(max_length=10, blank=False,default='')
    name        = models.CharField(max_length=50, blank=False,default='')
    email       = models.CharField(max_length=20, blank=False,default='')
    password    = models.CharField(max_length=50, blank=False,default='')

class Book(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name    = models.CharField(max_length=100, blank=False, default='')
    rls_date= models.DateTimeField()
    book_cat= models.CharField(max_length=5, blank=False, default='')
    publisher= models.CharField(max_length=20,default='')
    price   = models.IntegerField(blank=False)
    stock   = models.IntegerField(blank=True, default='10')

    class Meta:
        ordering = ('name',)

class Order(models.Model):
    order_name = models.CharField(max_length=30)
    user_order = models.ManyToManyField(User)
    date_order = models.DateTimeField(auto_now_add=True)

class Publisher(models.Model):
    pub_id = models.CharField(max_length=5, blank=False)
    name   = models.CharField(max_length=20, blank=False)

    class Meta:
        ordering = ('name',)

class UserLogin(AbstractUser):
    name = models.CharField(blank=True,max_length=255)

    def __str__(self)
        return self.email

