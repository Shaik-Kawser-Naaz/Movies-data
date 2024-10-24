from django.urls import path
from bollywood import views

urlpatterns=[
    path('movie',views.func1,name='p1')
]