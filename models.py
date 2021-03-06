from django.db import models

from djangotoolbox.fields import ListField, EmbeddedModelField
from django_mongodb_engine.contrib import MongoDBManager

class Id(models.Model):

    namespace = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

class Person(models.Model):

    objects = MongoDBManager()

    name = models.CharField(max_length=255)
    texts = ListField(EmbeddedModelField('TextSet'))
    ids = ListField(EmbeddedModelField('Id'))
    nameVariants = ListField()
    deepestPaths = ListField(EmbeddedModelField('Path'))
    # deepestPaths = ListField(DictField())

    class MongoMeta:

        indexes = [ [('name', 1)] ]

class Path(models.Model):

    edges = ListField(EmbeddedModelField('Edge'))

class Edge(models.Model):

    personName = models.CharField(max_length=255)
    endPersonName = models.CharField(max_length=255)
    weight = models.FloatField()

class Text(models.Model):

    objects = MongoDBManager()

    textId = models.CharField(max_length=255)
    authors = ListField(EmbeddedModelField('Person'))

    class MongoMeta:

        indexes = [ [('textId', 1)] ]

class TextSet(models.Model):

    label = models.CharField(max_length=255)
    value = models.FloatField()
    texts = ListField(EmbeddedModelField('Text'))
