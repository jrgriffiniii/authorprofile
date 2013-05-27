from django.db import models

from djangotoolbox.fields import ListField, EmbeddedModelField
from django_mongodb_engine.contrib import MongoDBManager

class Person(models.Model):

    objects = MongoDBManager()

    name = models.CharField(max_length=255)
    texts = ListField()
    ids = ListField(EmbeddedModelField('Id'))
    nameVariants = ListField()
    deepestPaths = ListField(EmbeddedModelField('Path'))

class Path(models.Model):

    edges = ListField(EmbeddedModelField('Edge'))

class Edge(models.Model):

    personName = models.CharField(max_length=255)
    weight = models.FloatField()

class Id(models.Model):

    namespace = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
