from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('projects/', views.projects, name="projects"),
    path('projects/<str:client_name>/', views.project_template, name="project_template"),
    path('team/', views.team, name="team"),
    path('<str:client_name>/', views.client_details, name='client_details'),
]




if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)