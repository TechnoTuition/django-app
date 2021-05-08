from blog import views 
from django.urls import path


#============,app url============
urlpatterns = [
    path('',views.blogHome , name="blogHome"),
    path('<str:slug>',views.blogPost,name="blogPost"),
    
]