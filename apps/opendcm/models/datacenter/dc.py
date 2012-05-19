from django.db import models
from django.conf import settings


class DataCenter(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    descr = models.CharField(max_length=4096, blank=True)

    def __unicode__(self):
        return u'%s-%s' % (self.name, self.city)

    class Meta:
        app_label = 'opendcm'
        # order ascending by order
        ordering = ['name']
        # add view permission (GET)
        permissions = (
           ("view_datacenter", "Can view avaliable datacenters"),
        )
