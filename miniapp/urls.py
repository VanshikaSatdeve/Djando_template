from django.urls import path
from . import views

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('posts/',views.postpage.as_view(),name='allposts'),
    path('posts/<slug:slug>',views.post_detail.as_view(),name='postsdetails'),
    path('create/', views.CreatePostView.as_view(), name='create_post'),
     path('success', views.success.as_view()),
  
]
