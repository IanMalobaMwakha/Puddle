from django.db import models

class Cartegory(models.Model):
    name = models.CharField(max_length=255)
