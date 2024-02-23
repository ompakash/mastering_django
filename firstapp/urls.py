from django.urls import path
from firstapp.models import *
from firstapp import views
urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('contactusclass/', views.ContactUs.as_view(), name="contactclass"),
    path('contactus/', views.contactus2, name="contact"),

    # Authentication Endpoints
    path('signup/', views.RegisterView.as_view(), name="signup"),
    path('login/', views.LoginViewUser.as_view(), name="login"),
    path('signupseller/', views.RegisterViewSeller.as_view(), name="signupseller"),
    path('logout/', views.LogoutViewUser.as_view(), name="logout"),

]
