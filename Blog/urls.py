from django.urls import path, re_path
from Blog import views

# TEMPLATE TAGGING
app_name = 'Blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<pk>/', views.post_detail, name='post_detail'),
    path('post/<pk>/edit/', views.post_edit, name='post_edit'),
]
