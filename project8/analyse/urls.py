from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('analyse_index/', views.analyse_index),
    path('analyse_register/', views.analyse_register),
    path('analyse_login/', views.analyse_login),
    path('view_PREDICTED/', views.view_PREDICTED),
    path('view_report/', views.view_report),
    path('view_final_report/', views.view_final_report),
    path('analyse_logout/', views.analyse_logout),
    # path('admin_update/', views.admin_update),
    path('find_report/<int:id>/', views.find_report),
    path('send_predicted_data/<int:id>/', views.send_predicted_data),

]
