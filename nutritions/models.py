from django.db import models
from django.urls import reverse

import jsonfield

class nutritions(models.Model):
    foodid = models.CharField(max_length=200)

    label = models.CharField(max_length=200)

    nutrients = jsonfield.JSONField()

    category = models.CharField(max_length=200)

    categoryLabel = models.CharField(max_length=200)

    image = models.URLField()
    
    def __str__(self):
        return self.label

    def get_absolute_url(self):
        return reverse("nutrition_detail", kwargs={"nutritions_id": self.pk})

