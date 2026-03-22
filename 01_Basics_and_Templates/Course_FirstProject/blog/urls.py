from django.urls import path
from blog import views
from django.views.generic import TemplateView

app_name = 'blog'

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', TemplateView.as_view(template_name='blog/about.html', extra_context={'site': 'mysite.com'}), name='about'),
    path('contact/', views.contact, name='contact'),
]