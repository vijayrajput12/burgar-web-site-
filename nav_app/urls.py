from .import views
from django.urls import path

urlpatterns=[
    path('',views.home1,name='home'),
    path('about',views.about1,name='about'),
    path('table',views.book,name='table'),
    path('menu',views.menu,name='meny')
    
]

