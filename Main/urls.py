from django.urls import path
from Main import views

# TEMPLATE TAGGING
app_name = 'Main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),

]
