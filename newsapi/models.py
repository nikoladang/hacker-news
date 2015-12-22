from django.db import models

# Create your models here.
class SavedEmbed(models.Model):
    type = models.CharField(max_length=15)
    provider_url = models.URLField()
    provider_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    html = models.TextField()
    width = models.IntegerField()
    height = models.IntegerField()
    thumbnail_url = models.URLField()
    thumbnail_width = models.IntegerField()
    thumbnail_height = models.IntegerField()
    author_url = models.URLField()
    author_name = models.CharField(max_length=100)
    version = models.DecimalField(max_digits=4, decimal_places=2)
