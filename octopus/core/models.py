from django.db import models

class Data(models.Model):
    meterPoint = models.CharField(max_length=100)
    meter = models.CharField(max_length=100)
    reading = models.FileField(upload_to='data/uffs')

    def __str__(self):
        return self.meterPoint
