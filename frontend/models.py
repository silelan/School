from django.db import models

# Create your models here.
class GalleryModel(models.Model):
    image_name = models.CharField(max_length = 100)
    image_description = models.CharField(max_length = 254)
    image = models.ImageField(upload_to = 'gallery',null=False)

    def __str__(self):
        return self.image_name