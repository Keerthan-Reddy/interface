from django.shortcuts import render, get_object_or_404
from base.models import Client, ImageWithLink, AnotherSetOfImages, NewProjects


def home(request):
    return render(request,'index.html')



def projects(request):
    return render(request,'projects.html')

def project_template(request, client_name):
    project = get_object_or_404(NewProjects, name=client_name)
    context = {'client_name': client_name, 'projecturl': project.projecturl}
    return render(request, 'projecttemplate.html', context)

def team(request):
    return render(request,'team.html')


def client_details(request, client_name):
    client = get_object_or_404(Client, name=client_name)
    # default_links = DefaultLink.objects.filter(client=client)
    image_links = ImageWithLink.objects.filter(client=client)
    other_images = AnotherSetOfImages.objects.filter(client=client)
    return render(request, 'home.html', {'client': client, 'image_links': image_links, 'other_images': other_images})
