from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('process_index/', views.process_index),
    path('view_o_detail/', views.view_o_detail),
    path('Process_register/', views.Process_register, name='Process_register'),
    path('Process_login/', views.Process_login),
    path('view_o_detail_PREDICTED/', views.view_o_detail_PREDICTED, name='view_o_detail_PREDICTED'),
    path('process_video_1/', views.process_video_1),
    path('process_logout/', views.process_logout),
    path('loader/', views.loader,name='loader'),
    path('redirect1/', views.redirect1),
    path('radioactive/', views.radioactive),
    path('view_o_detail_sent/', views.view_o_detail_sent),
    path('view_completed_isotope/', views.view_completed_isotope, name="view_completed_isotope"),
    path('get_input/<int:id>/', views.get_input),
    path('send_isotope/<int:id>/', views.send_isotope),
  


]