from django.urls import path
from . import views

app_name = 'adm'

urlpatterns = [
    path('', views.index, name='index_adm'),
    path('add/', views.add, name='add'),
    path('login/', views.login_adm, name='login_adm'),
    path('logout/', views.logout_adm, name='logout_adm'),
    path('register/', views.register, name='register'),

]
