from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home , name='home'),
    path('signin' , views.signin , name='signin'),
    path('signup' , views.signup , name='signup'),
    path('profile' , views.profile , name='profile'),
    path('welcomeSettings' , views.welcomeSettings , name='welcomeSettings'),
    path('forgetPassword' , views.forgetPassword , name='forgetPassword'),
    path('resetPassword/<token>/', views.resetPassword, name = 'resetPassword'),
    path('logout', views.logout_view, name = 'logout'),
    path('verify_email/<token>/', views.verify_email, name = 'verify_email'),
    path('about', views.about, name = 'about'),
    path('accountSettings', views.accountSettings, name = 'accountSettings'),
    path('changePassword', views.changePassword, name = 'changePassword'),
    path('home', views.home, name = 'home'),
    path('upload', views.upload, name='upload'),
]
