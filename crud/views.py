from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from . import models

# Create your views here.

class test(APIView):
    def get(self, request):
        return Response({"status":"hai"})



class CreateCategory(APIView):
    def get(self, request):
        data = CategoryManagement.objects.all()
        if data:
            category_serialize = CategorySerialize(data,many=True)
            return Response(category_serialize.data)
        return Response({"status":"category tabel is empty"})
    
    def post(self, request):
        category_name = request.data['category_name']
        print(category_name)
        data = CategoryManagement.objects.create(category_name=category_name)
        return Response({"status":"category addedd successfully"})

class EditDeleteCategory(APIView):
    def get(self, request, id):
        data = CategoryManagement.objects.filter(id=id)
        if data:
            serialize_data = CategorySerialize(data,many=True)
            return Response(serialize_data.data)
        else:
            return Response({"status":"No category"})

    def put(self, request, id):
        id = id
        category_name = request.data['category_name']
        data = CategoryManagement.objects.get(id=id)
        if data:
            data.category_name = category_name
            data.save()
            return Response({"status":"updated successfully "})
        else:
            
            return Response({"status":"unknown category"})

    def delete(self, request, id):
        id=id
        data = CategoryManagement.objects.get(id=id)
        data.delete()
        return Response({"status":"deleted successfully"})


class CreateSubcategory(APIView):
    def get(self, request):
        data = Subcategory.objects.all()
        if data:
            data_serialize = SubcategorySerialize(data,many=True)
            return Response(data_serialize.data)
        return Response({"status":"Subcategory table is empty"})
    def post(self, request):
        category_id = request.data['category_id']
        subcategory_name = request.data['subcategory_name']
        category = CategoryManagement.objects.get(id=category_id)
        if category:
            data = Subcategory.objects.create(category=category, subcategory_name=subcategory_name)
            return Response({"status":"subcategory created successfully"})
        return Response({"status":"category does not exist"})

class EditDeleteSubcategory(APIView):
    def get(self, request, id):
        id = id
        data = CategorySub.objects.filter(id=id)
        if data:
            serialize_data = SubcategorySerialize(data,many=True)
            return Response(serialize_data.data)
        return Response({"status":"subcategory does not exist"})



class CreateProduct(APIView):
    def get(self, request):
        data = Products.objects.all()
        if data:
            serialize_data = ProductSerialize(data,many=True)
            return Response(serialize_data.data)
        else:
            return Response({"status":"No products"})
    
    def post(self, request):
        category = request.data['category_id']
        product_name = request.data['product_name']
        price = request.data['price']
        description = request.data['description']
        # image = request.data['image']
        count_of_stock = request.data['count_of_stock']
        data = CategoryManagement.objects.get(id=category)
        print(data)
        data = Products.objects.create(product_name=product_name, price=price, description=description, count_of_stock=count_of_stock, category=data)
        return Response({"status":"product created successfully"})


class EditDeleteProduct(APIView):
    def get(self, request, id):
        id=id
        data = Products.objects.filter(id=id)
        if data:
            serialize_data = ProductSerialize(data,many=True)
            return Response(serialize_data.data)
        return Response({"status":"product does not exist"})

    def put(self, request, id):
        id = id
        category_id = request.data['category_id']
        product_name = request.data['product_name']
        price = request.data['price']
        description = request.data['description']
        # image = request.data['image']
        count_of_stock = request.data['count_of_stock']
        category = CategoryManagement.objects.get(id=category_id)
        data = Products.objects.get(id=id)
        print(data)
        if data:
            data.product_name = product_name
            data.price = price
            data.description = description
            data.count_of_stock = count_of_stock
            data.category = category
            data.save()
            return Response({"status":"updated successfully"})
        return Response({"status":"product does not exist"})

    def delete(self, request, id):
        id = id
        product = Products.objects.get(id=id)
        if product:
            product.delete()
            return Response({"status":"deleted successfully"})
        else:
            return Response({"statsu":"product does not exist"})



# def test(request):
#     data = Products.objects.get(price=47000)
#     print(data.category.category_name)
#     return HttpResponse("jhshg")