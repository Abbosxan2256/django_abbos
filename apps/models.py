from django.db.models import Model, CharField, BooleanField, ForeignKey, URLField, FloatField, ImageField
from django.db.models import CASCADE
from django_ckeditor_5.fields import CKEditor5Field


class Category(Model):
    name = CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(Model):
    name = CharField(verbose_name='nomi', max_length=255)
    description = CKEditor5Field(max_length=255)
    price = FloatField()
    category = ForeignKey('apps.Category', CASCADE)

    def __str__(self):
        return self.name


class ProductImage(Model):
    image = ImageField()
    product = ForeignKey('apps.Product', CASCADE)

    def __str__(self):
        return self.image


class Post(Model):
    user = ForeignKey('auth.User', CASCADE)
    title = CharField(max_length=255)
    body = CharField(max_length=255)


class Comment(Model):
    name = CharField(max_length=255)
    email = CharField(max_length=255)
    body = CharField(max_length=255)
    post = ForeignKey('apps.Post', CASCADE)


class Album(Model):
    user = ForeignKey('auth.User', CASCADE)
    title = CharField(max_length=255)


class Photo(Model):
    album = ForeignKey('apps.Album', CASCADE)
    title = CharField(max_length=255)
    urllib = URLField(verbose_name='Havola', max_length=255)
    thumbnailUrl = CharField(max_length=255)


class Todos(Model):
    user = ForeignKey('auth.User', CASCADE)
    title = CharField(max_length=255)
    completed = BooleanField(verbose_name='tugatilganmi')


class Person(Model):
    photo = ImageField(upload_to='image')
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    profession = CharField(max_length=255)

