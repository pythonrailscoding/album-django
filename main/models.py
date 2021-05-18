from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    image = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return str(self.category)


