from email.mime import image
from unittest.util import _MAX_LENGTH

from django.db import models
import datetime

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    mobile_no = models.CharField(max_length = 10)
    email_id = models.EmailField()
    password = models.CharField(max_length = 30)

    def register(self):
        self.save()

    def isExists(self):
        if Customer.objects.filter(email_id = self.email_id):
            return True
        else:
            return False
        
    


    @staticmethod
    def get_customer_by_email(email):
      try:
        return Customer.objects.get(email_id = email)
      except:
          return False
        
    

class Category(models.Model):
    name = models.CharField(max_length = 50)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 50)
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete = models.CASCADE,default = 1)
    description = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'upload/products/')

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
           return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in = ids)

class Order(models.Model):
    product = models.ForeignKey(Product,on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length = 50,default='',blank = True)
    phone = models.CharField(max_length=50,default='',blank = True)
    Date = models.DateField(default = datetime.datetime.today)

    

