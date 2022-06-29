from django.urls import path,include
from . import views

urlpatterns = [
    path('fatch',views.fatch_data,name='fatch'),
    path('',views.home),
    path('uploaddata',views.upload_csv,name='uploaddata'),
    

]