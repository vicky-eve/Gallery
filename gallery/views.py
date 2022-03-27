from django.shortcuts import render, redirect
from .models import Image, Location, Category
from django.http.response import Http404


# Create your views here.
def index(request):
    image=Image.objects.all()
    

    return render (request,'index.html',{'image':image})
def get_locatiopn(request, search_by_location):
    title="Location"
    location=Location.objects.all()
    image= Image.filter_by_location(search_by_location)
    message=f"(search_by_location )"
    return render (request, 'location.html', {"image":image, "location":location, "message":message, "title":title})

def get_image(request, image_id):
    try:
        image=Image.objects.get(id=image_id)
    except:
        raise Http404()
    return render (request, "image.html", {'image':image})

def get_category(request):
    title="Category"

    if 'category' in request.GET and request.GET["category"]:
        search_by_category=request.GET.get("category")
        category_search = Image.search_image(category_search)
        message= f"{category_search}"

        return render (request, 'search.html', {'message':message})