from django.contrib.auth.models import User
from django.db import models
class Author(models.Model):
    fullname = models.CharField(max_length=100)
    born_date = models.CharField(max_length=50)
    born_location = models.TextField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.fullname

class Tag(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)

    def __str__(self):
        return self.name

class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, null=True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.quote[:50]
