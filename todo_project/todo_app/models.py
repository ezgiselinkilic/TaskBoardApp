from django.db import models
from datetime import datetime
# Create your models here.
class Project(models.Model):
    project_name=models.TextField(max_length=1000)

    def __str__(self):
        return self.project_name
        
class Todos(models.Model):
    title=models.CharField(max_length=100)
    technical_specialist=models.CharField(max_length=150,blank=True)
    estimated_elapsed_time = models.CharField(max_length=100,blank=True)
    actual_time = models.CharField(max_length=100,blank=True)
    notes=models.TextField(max_length=1000,blank=True)
    state=models.CharField(max_length=100,blank=True)
    description=models.TextField(max_length=1000)
    finished= models.BooleanField(default=False)
    date=models.DateTimeField(default=datetime.now,blank=True)
    status=models.IntegerField(default=0,blank=True)
    project_name=models.ForeignKey(Project,on_delete=models.CASCADE)

    def __str__(self):
        return self.title


