from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact
from django.contrib import messages
from main.models import Post




# Create your views here.
def home(request):
    allPosts = Post.objects.all()
    context = {'allPosts' : allPosts}
    return render(request,'home/home.html',context)

def contact(request):
    
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<1:
            messages.error(request,"Please Fill The form correctly")
        else:
            contact=Contact()
            contact.name= name
            contact.email=email
            contact.phone=phone
            contact.content=content
            contact.save()
            messages.success(request,"Your message has been sent successfully")

        

    return render(request,'home/contact.html')

def aboutus(request):
    allPosts = Post.objects.all()
    context = {'allPosts' : allPosts}
    return render(request,'home/about.html',context)


def search(request):
    
    return (request,'home/search.html')
    #return HttpResponse("This is search")
