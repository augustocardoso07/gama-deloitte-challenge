from django.db import models


class Member(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=300)
    body = models.TextField()
    author = models.ForeignKey('Member', on_delete=models.DO_NOTHING)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
