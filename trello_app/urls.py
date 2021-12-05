from django.contrib import admin
from django.urls import path
from . import views
from django.urls.conf import include

urlpatterns = [
    # path('',views.index,name="index"),
    path('add_list/',views.create_list,name='create_list'),
    path('add_task/',views.create_task,name='create_task')

]