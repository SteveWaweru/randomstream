# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import random

# Create your models here.


class RandomNumber(models.Model):
    number = models.IntegerField(default=0)

    def update_number(self):
        self.number = random.randrange(0, 100)

    def __unicode__(self):
        return str(self.number)