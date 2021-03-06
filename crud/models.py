from django.db import models

# Create your models here.

class CategoryManagement(models.Model):
    category_name = models.CharField(max_length=128, null=True, blank=True)



class CategorySub(models.Model):
    category = models.ForeignKey(CategoryManagement, on_delete=models.CASCADE, blank=True, null=True,)
    subcategory_name = models.CharField(max_length=128, null=True, blank=True)

class Products(models.Model):
    category = models.ForeignKey(CategoryManagement, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(CategorySub, on_delete=models.CASCADE, blank=True, null=True)
    product_name = models.CharField(max_length=128, null=True, blank=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    is_available = models.BooleanField(null=True, blank=True, default=True)
    count_of_stock = models.IntegerField(blank=True, null=True)

    @property
    def ImageURL(self):
        try:
            url= self.image.url
        except:
            url=''
        return url



# {"category_name":"mobile",
# "count_of_stock":100}