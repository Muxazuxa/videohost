from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Home(models.Model):
    video = models.CharField(max_length=10000)
    name = models.CharField(max_length=50, default="Vidos")
    user = models.ForeignKey(User, on_delete=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
