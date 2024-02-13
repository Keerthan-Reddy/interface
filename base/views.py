from django.shortcuts import render, get_object_or_404
from .models import Client, ImageWithLink, AnotherSetOfImages

def home(request):
    return render(request,'home.html')


def client_details(request, client_name):
    client = get_object_or_404(Client, name=client_name)
    # default_links = DefaultLink.objects.filter(client=client)
    image_links = ImageWithLink.objects.filter(client=client)
    other_images = AnotherSetOfImages.objects.filter(client=client)
    return render(request, 'home.html', {'client': client, 'image_links': image_links, 'other_images': other_images})
