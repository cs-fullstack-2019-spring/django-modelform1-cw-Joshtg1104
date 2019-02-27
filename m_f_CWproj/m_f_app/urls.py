from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # path for the index function and newPost.html
    path('blogEntry/', views.index, name='index'),  # path for blogEntry.html
]
