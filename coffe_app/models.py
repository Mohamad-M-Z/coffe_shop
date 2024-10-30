from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Menu(models.Model):
    image = models.ImageField(upload_to='media/menu/', default='menu/menu-1.jpg')
    name = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    content = models.TextField()
    price = models.IntegerField()
    status = models.BooleanField(default=False)
    login_require = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
