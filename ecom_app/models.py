from django.db import models

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_category = models.CharField(max_length=50,  default="")
    product_price = models.IntegerField( default=0)
    product_description = models.CharField(max_length=300)
    product_publish_date = models.DateField()
    product_image = models.ImageField(upload_to="static/product/images", default="")

    def __str__(self):
        return self.product_name