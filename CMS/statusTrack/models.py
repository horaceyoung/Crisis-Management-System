from django.db import models


class Step01(models.Model):
    department = models.CharField(max_length=500)

class Step02(models.Model):
    plan = models.CharField(max_length=9999)

class Step03(models.Model):
    work = models.CharField(max_length=9999)

class step04(models.Model):
    status = models.CharField(max_length=9)

