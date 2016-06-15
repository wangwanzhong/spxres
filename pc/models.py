from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    department = models.ForeignKey(Department)
    usage = models.CharField(max_length=50)
    cpu = models.CharField(max_length=50)
    board = models.CharField(max_length=50)
    mem = models.CharField(max_length=50)
    disk = models.CharField(max_length=50)
    display = models.CharField(max_length=50)
    history_usage = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=50, blank=True)
    up_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.usage
