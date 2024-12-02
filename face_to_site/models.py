from django.db import models


class Category(models.Model):
    category_genre = models.CharField(max_length=50)
    image_category = models.ImageField(upload_to='images/', default=None)

    def __str__(self):
        return self.category_genre

