from django.db import models

# Create your models here.
class Character(models.Model):
    name = models.CharField(max_length=50, unique=True)
    img_url = models.CharField(max_length=100)

    # This tells Django Admin (and other things) how to display each object
    # (e.g. 'Kirk' rather than 'Character object')
    def __unicode__(self):
        return self.name