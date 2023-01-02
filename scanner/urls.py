from django.urls import path

from . import views

urlpatterns = [
    path('scan', views.scanner, name='scanner'),
    path('AjaxDorkScan',views.AjaxDorkScan,name="AjaxDorkScan")
]
