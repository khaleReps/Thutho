from django.urls import path
from . import views


urlpatterns = [

    path('index', views.index, name='index'),
    path('pricing', views.pricing, name='pricing'),


    path('change-password', views.change_password, name='change-password'),
    path('login', views.login, name='login'),
    path('reset-password', views.reset_password, name='reset-password'),
    path('signup', views.signup, name='signup'),
    path('signup-payment', views.signup_payment, name='signup-payment'),

 
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('products/', views.products, name='products'),
    path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),


]