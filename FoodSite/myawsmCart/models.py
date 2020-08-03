from django.db import models

class Products(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=50)
    desc=models.CharField(max_length=380)
    pub_date=models.DateField()
    category=models.CharField(max_length=50,default="")
    sub_category=models.CharField(max_length=50,default="")
    price=models.IntegerField(default=0)
    image=models.ImageField(upload_to="foodsite/images",default="")

    def __str__(self):
        return self.product_name
