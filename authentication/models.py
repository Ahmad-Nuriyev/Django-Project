from django.db import models

# Create your models here.

class BlockedIPAdresses(models.Model):
    ip_adress = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_adress