from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator,MinValueValidator

# Create your models here.

STATE_CHOICES = (('kl','Kerala'),('tn','Tamil Nadu'))

class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=60)
    adefault = models.CharField(max_length=5,default='No')

    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICES = (
    ('a','Android Phones'),
    ('i','Iphones'),
    ('q','QWERTY Phones'),
    ('k','Keypad Phones')
) 

BRAND_CHOICES = (
    ('Xiaomi','Xiaomi'),
    ('Samsung','Samsung'),
    ('Huawei','Huawei'),
    ('Oppo','Oppo'),
    ('Apple','Apple'),
    ('Oneplus','Oneplus'),
    ('Realme','Realme'),
    ('Pocco','Pocco'),
    ('Lenovo','Lenovo'),
    ('Nokia','Nokia'),
    ('Jio','Jio')

)


class Product(models.Model):
    title = models.CharField(max_length=100)
    s_price = models.FloatField()
    d_price = models.FloatField()
    brand = models.CharField(max_length=30,choices=BRAND_CHOICES)
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    soc = models.CharField(max_length=200)
    ram = models.CharField(max_length=20)
    connectivity = models.CharField(max_length=200)
    battery = models.CharField(max_length=100)
    screen = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    rom = models.CharField(max_length=20)
    osystem = models.CharField(max_length=50)
    product_img = models.ImageField(upload_to='productimg')

    def __str__(self):
        return str(self.title)

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On The Way','On The Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel')
    
) 


class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,
    default='Pending')





