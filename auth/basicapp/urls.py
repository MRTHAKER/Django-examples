from django.urls import path
from . import views

app_name='basicapp'
urlpatterns=[path('',views.index,name='index'),
path('register',views.register,name='register'),
path('login_user',views.login_user,name='login'),
path('logout_user',views.logout_user,name='logout'),
path('dashboard',views.dashboard,name='dashboard'),
]
