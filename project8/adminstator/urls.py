from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('a_index/', views.a_index),
    path('admin_login/', views.admin_login),
    path('view_org_file_admin/', views.view_org_file_admin),
    path('download/<int:id>/', views.download),
    path('access_o/<int:id>/', views.access_o),
    path('clear/<int:id>/', views.clear),
    path('admin_request/', views.admin_request),
    path('view_org_details/', views.view_org_details),
    path('view_org_details_approved/', views.view_org_details_approved),
    path('A_logout/', views.A_logout),
    path('payslip/', views.payslip),

]