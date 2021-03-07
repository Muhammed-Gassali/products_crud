from rest_framework import serializers
from .models import *


class CategorySerialize(serializers.ModelSerializer):
    class Meta:
        model = CategoryManagement
        fields = ('category_name',)

class ProductSerialize(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('product_name','price','description','id','category')
    
class SubcategorySerialize(serializers.ModelSerializer):
    class Meta:
        model = CategorySub
        fields = ('category','subcategory_name')
