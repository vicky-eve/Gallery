from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='Home'),
    path('search/', views.get_category, name='category'),
    path('location/<str:search_by_location>/', views.get_location,name='location'),
    path('image/<int:image_id>/',views.get_image, name='image'),
]
if settings.debug:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)