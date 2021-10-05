from django.shortcuts import render, redirect
from .models import Category, Photo
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(
            category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'album/gallery.html', context)


def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'album/photo.html', {'photo': photo})


def addPhoto(request):

    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images')
        if data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        elif data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        else:
            category = None


        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('gallery')

    context = {'categories': categories}
    return render(request, 'album/add.html', context)