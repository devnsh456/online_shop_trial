from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)

    def __str__(self):
        return self.name


# def upload_image_to(instance)
class Product(models.Model):
    name=models.CharField(max_length=250,)
    product_code=models.CharField(max_length=15,unique=True)
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)

    product_image=models.ImageField(upload_to='products/')
    price=models.DecimalField(max_digits=10,decimal_places=2)
    available=models.BooleanField(default=True)

    class Meta:
        ordering:('name',)

    def __str__(self):
        return self.name
