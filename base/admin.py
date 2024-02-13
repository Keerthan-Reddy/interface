from django.contrib import admin
from .models import Client, ImageWithLink, AnotherSetOfImages

admin.site.register(Client)
admin.site.register(ImageWithLink)
admin.site.register(AnotherSetOfImages)
