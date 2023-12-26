from django.urls import path

from Googleai import views

urlpatterns = [
    path('',views.home,name='home'),
    path('search',views.send_prompt,name='prompt')
]