from django.db import models

class ListingItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='listing_images/')
    video = models.FileField(upload_to='media/videos/', default='default_video.mp4')

    def __str__(self):
        return self.title
