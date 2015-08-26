from django.db import models

# Create your models here.
class Chart(models.Model):
    name = models.CharField(max_length=50, unique=True)
    img_url = models.CharField(max_length=100)
    chart_type = models.CharField(max_length=50)

    # This tells Django Admin (and other things) how to display each object
    def __unicode__(self):
        return self.name