from django.db import models

# Create your models here.
class Resume(models.Model):
    title = models.CharField(max_length=100)
    price = models.TextField()
    desc = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.title} {self.price} {self.desc}"