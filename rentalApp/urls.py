from django.urls import path
from . import views as v


urlpatterns = [
    path('', v.index, name='index'),
    path('services', v.services, name='services'),
    path('pricing', v.pricing, name='pricing'),
    path('contact', v.contact, name='contact'),
    path('car', v.car, name='car'),
    path('about', v.about, name='about'),
    path('car_detail/<int:car_id>/', v.car_detail, name='car_detail'),
    path('blog', v.blog, name='blog'),
    path('review/<int:car_id>/', v.review, name='review'),
    path('booking/<int:car_id>/', v.booking, name='booking'),
    path('blog_detail/<int:blog_id>/', v.blog_detail, name='blog_detail'),
    path('category_detail/<int:cat_id>/', v.category_detail, name='category_detail'),
    
]