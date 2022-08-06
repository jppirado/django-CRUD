from django.urls import path 

from .views import list_products, edit_products , dethalis_product , insert_products , delete_products, create_products, list_products_delete, success_page ,  update_products 

urlpatterns = [
    path('' , insert_products , name="inserir" ),
    path('success' , success_page , name='success' ),
    path('list' , list_products , name="list"),
    path('listaDelete' , list_products_delete , name='products_delete' ),
    path('dethalis/<int:pk>/' , dethalis_product , name="dethalis"),
    path('create/' ,create_products , name="create"),
    path('edit/<int:pk>/' , edit_products , name="edit"),
    path('update/<int:pk>/' ,update_products , name="updateProducts"),
    path('delete/<int:pk>/' ,delete_products , name="deleteProducts"),
    
]
