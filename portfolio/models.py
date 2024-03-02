from django.db import models
from django.utils import timezone
from django.shortcuts import redirect
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=500)

    def __str__(self):
        return self.category

class Project(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='projects')
    sub_category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True,related_name='subprojects')
    title = models.CharField(max_length=256)
    abstract = models.TextField(blank=True)
    codelink = models.URLField(blank=True)
    publish_date = models.DateField(default=False)  #to save draft
    #approved = models.BooleanField(default=False) #to publish saved
    img = models.ImageField(upload_to='display_pic',blank=True,null=True)
    fulltext = models.URLField(blank=True)
    
    def get_absolute_url(self):
        return reverse('portfolio:list_view')
    
    def __str__(self):
        return self.title
