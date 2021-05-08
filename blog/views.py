from django.shortcuts import render,HttpResponse
from blog.models import Post
# Create your views here.
def blogHome(request):
    allPost = Post.objects.all()
    contaxt = {"allPost":allPost}
    return render(request,"blog/blogHome.html", contaxt)
    
#================================#================================

def blogPost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    contaxt = {"post":post}
    return render(request,"blog/blogPost.html",contaxt)
    
    
