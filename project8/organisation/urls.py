from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('organisation_register/', views.organisation_register),
    path('organisation_login/', views.organisation_login),
    path('org_index/', views.org_index),
    path('org_details/', views.org_details),
    path('org_purpose_Details/', views.org_purpose_Details),
    path('org_logout/', views.org_logout),
    path('pay/', views.pay),
    path('view_DAta/', views.view_DAta),
    path('dec11/<int:id>/', views.dec11),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)