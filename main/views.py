from django.shortcuts import render
from django.http import HttpResponse
from main.models import Post
def main(request):
    allPosts = Post.objects.all()
    context = {'allPosts' : allPosts}
    return render(request,'main/mainhome.html', context)


def mainpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context={'post':post}
    return render(request,'main/mainpost.html',context)
    