from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=265)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    subject = models.CharField(max_length=265, null=True, blank=True)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


