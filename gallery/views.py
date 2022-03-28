from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
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
    if 'category' in request.GET and request.GET["category"]:
        # change the search to be in lowercase
        search_term = request.GET.get("category").lower()
        searched_images = Image.filter_by_category(search_term)
        message = f"{search_term}"
        location = Location.objects.all()
        return render(request, 'search.html', {"message": message, "images": searched_images, 'location': location})
    else:
        location = Location.objects.all()
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message, 'location': location})