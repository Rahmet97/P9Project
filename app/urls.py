from django.urls import path
from .views import Home, Contact, About, ProductDetail


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('contact', Contact.as_view(), name='contact'),
    path('about', About.as_view(), name='about'),
    path('product-detail/<int:pk>', ProductDetail.as_view(), name='product-detail')
]