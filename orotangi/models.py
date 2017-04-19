# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


class Books(models.Model):
    """
        Book
    """
    user = models.ForeignKey(User)
    name = models.CharField(max_length=80)
    date_created = models.DateField(auto_now_add=True)
    date_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        db_table = 'oro_books'


class Notes(models.Model):

    """
        Notes
    """
    user = models.ForeignKey(User)
    book = models.ForeignKey(Books)
    url = models.URLField(max_length=255, blank=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "%s - %s" % (self.book, self.title)

    class Meta:
        ordering = ('-date_created', )
        db_table = 'oro_notes'
