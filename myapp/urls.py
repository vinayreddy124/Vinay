from django.urls import path
from . import views


urlpatterns=[
    path('',views.login_view,name='login_view'),
    path('dealer_signup',views.dealer_signup, name='dealer_signup'),
    path('user_signup', views.user_signup, name='user_signup')
]