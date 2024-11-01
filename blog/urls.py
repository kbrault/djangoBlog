# blog/urls.py
from django.urls import path
from .views import post_list, post_detail  # Import function-based views

urlpatterns = [
    path('', post_list, name='post_list'),  # List of posts
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', post_detail, name='post_detail'),  # Post detail view
]
