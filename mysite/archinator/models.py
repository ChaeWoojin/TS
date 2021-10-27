from django.db import models
from django.utils import timezone

# Create your models here.

class Part(models.Model): ##부위
    name=models.CharField(max_length=200)
    create_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Category(models.Model): ##세부 분류
    part=models.ForeignKey(Part, on_delete=models.CASCADE)
    symptom=models.TextField()
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.symptom