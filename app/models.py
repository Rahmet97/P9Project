from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class District(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}|{self.region.name}'


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):

    sale_rent = (
        (1, 'For Sale'),
        (2, 'For Rent')
    )

    address = models.CharField(max_length=150)
    price = models.FloatField()
    image1 = models.ImageField(upload_to='pics')
    image2 = models.ImageField(upload_to='pics')
    image3 = models.ImageField(upload_to='pics', blank=True, null=True)
    image4 = models.ImageField(upload_to='pics', blank=True, null=True)
    image5 = models.ImageField(upload_to='pics', blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    description = models.TextField()
    sale_rent = models.IntegerField(choices=sale_rent)

    def __str__(self):
        return self.address
    

class ProductInfo(models.Model):
    room_count = models.IntegerField(default=1)
    bath_room = models.IntegerField(default=1)
    has_garage = models.BooleanField(default=False)
    square = models.FloatField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.address


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class UserProductView(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.address