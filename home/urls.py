from home import views 
from django.urls import path , include

urlpatterns = [
    path('',views.index , name="index"),
    path('contact/',views.contact , name="contact"),
    path('about/',views.about , name="about"),
    path("signup/",views.signup, name="signup"),
    path("Login/",views.Login,name="Login"),
    path("Logout/",views.Logout,name="Logout"),
    path("api/",views.api , name="api")
   
]


