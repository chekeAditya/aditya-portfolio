# Create your models here.
from django.db import models

# Defines your database structure in Python code Android Equivalent: Like Room entities Background: Django converts these to SQL tables automatically

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.JSONField()  # Store as ["Android", "Kotlin", "Firebase"]
    github_url = models.URLField(blank=True)
    play_store_url = models.URLField(blank=True)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)  # "Frontend", "Backend", "Mobile"
    proficiency = models.IntegerField()  # 1-100

    def __str__(self):
        return self.name
