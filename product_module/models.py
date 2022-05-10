from django.db import models

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to="product_image/", null=False, blank=False)
    description = models.TextField()
    price = models.PositiveIntegerField()
    is_active = models.BooleanField()

    def __str__(self):
        return self.product_name

    