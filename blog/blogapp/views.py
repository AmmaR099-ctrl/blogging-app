from django.shortcuts import render
from .models import post

def home(request):
    posts =post.objects.all()
    content={
        'title':"The Bloging App",
        'posts':posts
    }
    return render(request,'home.html',content)
def about(request):
    content={
        'title':"About this app:",
        'message':"This bloging will contain updated bloging."
    }
    return render(request,'about.html',content)
def contact(request):
    return render(request,'contact.html')
def post_detail(request,post_id ):
    Post=post.objects.get(id=post_id)
    content={'post':Post}
    return render(request,'post_detail.html',content)