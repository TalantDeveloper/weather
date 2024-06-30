from django.db import models


class Condition(models.Model):
    code = models.IntegerField(verbose_name='Code')
    text = models.CharField(max_length=255, verbose_name='text')

    def __str__(self):
        return str(self.code)
