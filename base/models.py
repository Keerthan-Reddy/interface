from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100, default="")  
    number = models.CharField(max_length=20)
    info = models.TextField()
    location = models.CharField(max_length=255)
    website = models.URLField()
    default_link = models.URLField(default="",max_length=1000)
    logoimage = models.ImageField(upload_to='logos/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class ImageWithLink(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    url = models.URLField(max_length=1000)
    
    def __str__(self):
        count = ImageWithLink.objects.filter(client=self.client).count()
        duplicate_count = ImageWithLink.objects.filter(client=self.client, id__lt=self.id).count()
        if count > 1:
            return f"image with link : {self.client} ({duplicate_count + 1})"
        else:
            return f"image with link : {self.client}"
        
class NewProjects(models.Model):
    name = models.CharField(max_length=100, default="")
    projecturl = models.URLField(max_length=1000)
    
    def __str__(self):
        return self.name
    
    
    

class AnotherSetOfImages(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        count = ImageWithLink.objects.filter(client=self.client).count()
        duplicate_count = ImageWithLink.objects.filter(client=self.client, id__lt=self.id).count()
        if count > 1:
            return f"gallery : {self.client} ({duplicate_count + 1})"
        else:
            return f"gallery : {self.client}"
