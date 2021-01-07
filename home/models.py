from django.db import models

# Create your models here.
class Apps(models.Model):
    app_name = models.CharField(max_length=30)
    description = models.CharField(max_length=500)
    last_updated = models.DateField()
    # image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.app_name

    def __unicode__(self):
        return 
