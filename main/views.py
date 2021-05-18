from django.shortcuts import redirect, render
from .models import Category, Photo

def index(request):
    cat_determine = request.GET.get("cat")
    if cat_determine == None:
        photo_list = Photo.objects.all()
    else:
        photo_list = Photo.objects.filter(category__name=cat_determine)
    cat_list = Category.objects.all() 
    return render(request, 'index.html', {'cat_list':cat_list, 'photo_list':photo_list})

def create(request):
    cat_list = Category.objects.all()
    if request.method == 'POST':
        description = request.POST
        image = request.FILES.get('formFile')
        if description['exist_cat'] != "none":
            cat = Category.objects.get(id=description['exist_cat'])
        elif description['category'] != '':
            cat, created = Category.objects.get_or_create(name=description['category'])
        else:
            cat = None
        
        photo = Photo.objects.create(category=cat, description=description['description'], image=image)
        photo.save()
        return redirect("index")
    return render(request, 'create.html', {'cat_list': cat_list})

def view(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'view.html', {'photo': photo})
