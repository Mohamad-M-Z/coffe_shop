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


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email



class Reservation(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    date = models.DateTimeField(default=False)
    time = models.TimeField(blank=True)
    choice_field = models.CharField( max_length=10)

    def __str__(self):
        return self.name


