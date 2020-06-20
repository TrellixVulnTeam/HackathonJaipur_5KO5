from django.urls import path
from app import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('registration',views.registration,name='registration'),
    path('patient',views.patient,name='patient'),
    path('login',views.LogIn,name='login')
]
