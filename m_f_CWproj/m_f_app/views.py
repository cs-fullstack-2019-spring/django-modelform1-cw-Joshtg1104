from django.http import HttpResponse
from django.shortcuts import render
from .forms import NewPostForm


# Create your views here.
# index function that applies the form "NewPostForm" to newPost.html
def index(request):
    newPost = NewPostForm()
    if request.method == "POST":
        print("It works")
        newPost = NewPostForm(request.POST)
        if newPost.is_valid():
            newPost.save(commit=True)
            return render(request, "m_f_app/blogEntry.html")  # render blogEntry.html once post is entered
    else:
        context = {
            "posts": newPost
        }
        return render(request, "m_f_app/newPost.html", context)
