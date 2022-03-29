from django.http import  HttpResponseRedirect
from django.shortcuts import render
from .models import Image, Location, Category
from django.http.response import Http404
from gallery.forms import ImageForm


# Create your views here.
def index(request):
    images=Image.objects.all()

    return render (request,'index.html',{'images':images})

def get_location(request, filter_location):
    title="Location"
    location=Location.objects.all()
    image= Image.filter_by_location(filter_location)
    message=f"(search_by_location )"
    return render (request, 'location.html', {"image":image, "location":location, "message":message, "title":title})

def get_image(request, image_id):
    try:
        images=Image.objects.get(id=image_id)
    except:
        raise Http404()
    return render (request, "image.html", {'images':images})



def new_image(request):
    if request.method=='POST':
        form=ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        return HttpResponseRedirect ('/')
    else:
        form=ImageForm()
    return render(request, 'new_image.html', {'form':form})

# search function to search for images
def search(request):
    if 'category' in request.GET and request.GET["images"]:
       
        search_category = request.GET.get("category")
        category_search = Image.search_by_category(search_category)
        message = f"{search_category}"
        return render(request, 'search.html', {"message": message, "images":category_search})
    else:
        message = "No category searched"
        return render(request, 'search.html', {"message": message})