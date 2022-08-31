from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home , name='home'),
    path('signin' , views.signin , name='signin'),
    path('signup' , views.signup , name='signup'),
    # path('profile' , views.profile , name='profile'),
    path('welcomeSettings' , views.welcomeSettings , name='welcomeSettings'),
    path('forgetPassword' , views.forgetPassword , name='forgetPassword'),
    path('resetPassword/<token>/', views.resetPassword, name = 'resetPassword'),
    path('logout', views.logout_view, name = 'logout'),
    path('verify_email/<token>/', views.verify_email, name = 'verify_email'),
    # path('about', views.about, name = 'about'),
    path('accountSettings', views.accountSettings, name = 'accountSettings'),
    path('changePassword', views.changePassword, name = 'changePassword'),
    path('home', views.home, name = 'home'),
    path('<name>/upload', views.upload, name='upload'),
    path('like', views.like, name='like'),
    path('deletepost', views.deletepost, name='deletepost'),
    path('profile/<name>' , views.profiletest , name='profiletest'),
    path('about/<name>' , views.about , name='about'),
    path('follow' , views.follow , name='follow'),
    path('search' , views.search , name='search'),
    path('follower/<name>' , views.follower , name='follower'),
    path('following/<name>' , views.following , name='following'),
    path('post/<id>' , views.post , name='post'),
    path('notification' , views.notification , name='notification'),
    path('Liked' , views.Liked , name='Liked'),
    path('comment' , views.comment , name='comment'),
    path('sendMessage' , views.sendMessage , name='sendMessage'),
]
