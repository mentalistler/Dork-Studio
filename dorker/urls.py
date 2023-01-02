from django.urls import path

from . import views

urlpatterns = [
    path('', views.dorker, name='index'),
    path('dorker/', views.dorker, name='dorker'),
    path('result/',views.dorkresults,name='dorkresults'),
    path('dorks/list',views.dorklist, name='dorklist'),
    path('dorks/<int:pk>',views.dorkdetail, name='dorkdetail'),
    
    path('dorks/add/',views.DorkAdd, name='dorkadd'),
    path('wordlist/',views.wordlistdetail, name='wordlistdetail'),

    path('wordlist/add/',views.WordlistAdd, name='wordlistadd'),
     ##Ajax
    path('AjaxTrendQuery/',views.AjaxTrendQuery,name='AjaxTrendQuery'),
    path('AjaxRemoveDork/<int:pk>',views.AjaxRemoveDork,name='AjaxRemoveDork'),
    path('AjaxAddDork/',views.AjaxAddDork,name='AjaxAddDork'),
    path('AjaxAddWordlist/',views.AjaxAddWordlist,name='AjaxAddWordlist'),
]
