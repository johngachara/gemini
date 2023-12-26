from django.db import models

# Create your models here.
class Prompts(models.Model):
    text = models.TextField()
    response = models.TextField(default='Response')
    def __str__(self):
        return self.text