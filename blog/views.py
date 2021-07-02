from django.shortcuts import render,HttpResponse
from blog.models import Post
# Create your views here.
def blogHome(request):
    allPost = Post.objects.all()
    contaxt = {"allPost":allPost}
    return render(request,"blog/blogHome.html", contaxt)
    
#================================#================================

def writePost(request):
    return render(request,"blog/writePost.html")
def blogPost(request,slugg):
    post = Post.objects.filter(slug=slugg).first()
    
    contaxt = {"post":post}
    return render(request,"blog/blogPost.html",contaxt)
    
    
