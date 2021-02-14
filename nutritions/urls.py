from django.urls import path

from . import views

    
urlpatterns = [
    path('', views.index, name='index'),
    path('fetch', views.fetch, name='fetch'),
    path('dupli', views.dupli, name='dupli'),
    path('<nutritions_id>/',views.detail, name='nutrition_detail'),
]