from django.contrib import admin
from .models import Client, ImageWithLink, AnotherSetOfImages, NewProjects

admin.site.register(Client)
admin.site.register(ImageWithLink)
admin.site.register(AnotherSetOfImages)
admin.site.register(NewProjects)
