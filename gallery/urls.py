from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('search/', views.search, name='category'),
    path('location/<str:filter_location>/', views.get_location,name='location'),
    path('image/<int:image_id>/',views.get_image, name='image'),
    path('new_image/', views.new_image, name='new_image')
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)