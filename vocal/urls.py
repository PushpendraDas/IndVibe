from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Home'),
    #path('product/', views.Details_Image),
    path('Addproduct/', views.Product, name="Addproduct"),
    path('showHome',views.showHome,name='showHome'),
    path('showBeauty',views.showBeauty,name='showBeauty'),
    path('showSanitry',views.showSanitry,name='showSanitry'),
    path('showStationary',views.showStationary,name='showStationary'),
    #path('product/', views.Details_Image),
]