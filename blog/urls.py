from blog import views 
from django.urls import path


#============,app url============
urlpatterns = [
    path('',views.blogHome , name="blogHome"),
    path("writePost",views.writePost,name="writePost"),
    path('<str:slugg>',views.blogPost,name="blogPost"),
    
]