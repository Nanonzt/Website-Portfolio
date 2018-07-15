from django.contrib import admin
from django.urls import path, include
from Main import views


urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
    path('Blog/', include('Blog.urls')),
    # path('Gallery/', include('Gallery.urls')),
]
