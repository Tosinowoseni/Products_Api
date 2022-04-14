from django.urls import path 
from . import views

urlpatterns = [
    path('', views.products_list.as_view),
    path('<int:pk>/'), views.ProductById.as_view())
]