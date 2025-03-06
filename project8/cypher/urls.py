from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('cypher_index/', views.cypher_index),
    path('Cypherr_register/', views.Cypherr_register),
    path('Cypher_login/', views.Cypher_login),
    path('view_file_domain/', views.view_file_domain),
    path('Encrypt_file/', views.Encrypt_file),
    path('view_admin/', views.view_admin),
    path('Cypher_logout/', views.Cypher_logout),
    path('admin_update/', views.admin_update),
    path('from_testing/', views.from_testing),
    path('ENCRYPTED/', views.ENCRYPTED),
    path('forwarded_data/', views.forwarded_data),
    path('enc/<int:id>/', views.enc),
    path('admin_send_mail/<int:id>/', views.admin_send_mail),
    path('send_admin1/<int:id>/', views.send_admin1),

]