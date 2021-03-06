from django.urls import path
from . import views

urlpatterns = [
    path('', views.CreateCategory.as_view(), name="category-management"),
    path('edit-delete-category/<int:id>', views.EditDeleteCategory.as_view(), name="edit-delete-category"),
    path('create-product', views.CreateProduct.as_view(), name="create-product"),
    path('edit-delete-product/<int:id>', views.EditDeleteProduct.as_view(), name="edit-delete-product"),
    path('create-subcategory', views.CreateSubcategory.as_view(), name="create-subcategory"),
    path('edit-delete-subcategory/<int:id>', views.EditDeleteSubcategory.as_view(), name="edit-delete-subcategory"),
    path('test', views.test, name="test"),
]