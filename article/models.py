from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.utils import timezone

# class Searches(models.Model):
#     title = models.CharField(max_length=225)
#
#     def __str__(self):
#         return self.title


# class Feeds(models.Model):
#     image = models.ImageField(upload_to='article/')
#     auther = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_date = models.DateTimeField(auto_now_add=True)
#     link = models.URLField()
#
#     def __str__(self):
#         return self.image


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='author/')
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(editable=False, null=True, blank=True)
    image = models.ImageField(upload_to='articles/')
    title = models.CharField(max_length=255)
    first_content = RichTextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='articles/comments/', null=True, blank=True)
    massage = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_image(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}" target="_blank"><img src="{self.image.url}" width="50" height="50"></a>')
        return '-'

    @property
    def children(self):
        if self.parent:
            return Comments.objects.filter(top_level_comment_id=self.id)
        return None


def article_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(article_pre_save, sender=Article)


def comment_pre_save(sender, instance, *args, **kwargs):
    if instance.parent:
        if instance.parent.top_level_comment_id:
            instance.top_level_comment_id = instance.parent.top_level_comment_id
        else:
            instance.top_level_comment_id = instance.parent.id


pre_save.connect(comment_pre_save, sender=Comments)

