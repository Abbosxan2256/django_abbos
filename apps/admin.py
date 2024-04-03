from django.contrib import admin
from apps.models import Product, Category, ProductImage, Post, Comment, Photo, Album, Todos, Person


# from import_export.admin import ImportExportModelAdmin


@admin.register(Category)
class CategoryModeL(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


class ProductImagesStackedInline(admin.StackedInline):
    model = ProductImage
    extra = 1
    max_num = 1
    min_num = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']
    inlines = [ProductImagesStackedInline]


class CommentInfoStackedInline(admin.StackedInline):
    model = Comment
    extra = 1
    max_num = 1
    min_num = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInfoStackedInline]


class PhotoImageStackedInline(admin.StackedInline):
    model = Photo
    extra = 1
    max_num = 1
    min_num = 1


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoImageStackedInline]


@admin.register(Todos)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(Person)
class Admin(admin.ModelAdmin):
    pass
