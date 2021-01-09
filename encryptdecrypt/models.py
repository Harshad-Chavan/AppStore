from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Action(models.Model):
    action = models.CharField(max_length=10)
    def __str__(self):
        return self.action
    
class FileDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    file_name  = models.CharField(blank=True,max_length=50)
    selected_action = models.ForeignKey(Action, on_delete=models.CASCADE)
    key  = models.CharField(blank=True,max_length=50)   
    def __str__(self):
        return self.file_name
    

