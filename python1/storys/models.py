from django.db import models

# Create your models here.
class Story(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=5000)
    def __unicode__(self):
        return self.title