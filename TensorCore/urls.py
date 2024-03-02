
from django.contrib import admin
from django.urls import path
from django.conf.urls import include 
from portfolio import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.FrontPageView.as_view(),name='home'),
    path('admin/', admin.site.urls),
    path('portfolio/',include('portfolio.urls')),
    path('account/login',LoginView.as_view(),name='login'),
    path('account/logout',LogoutView.as_view(),name='logout',kwargs={'next_page':'/'}),
    path('account/signup',views.UserSignupView.as_view(),name='signup'),
]
