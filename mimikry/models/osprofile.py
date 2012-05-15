from django.db import models
from django.conf import settings

class OSProfile(models.Model):
    name = models.CharField(max_length=100)
    pxe_file = models.CharField(max_length=100)
    pxe_cfg = models.CharField(max_length=100)
    description = models.CharField(max_length=4096, blank=True)            
    def __unicode__(self):
        return u'%s' % (self.name)
        
    class Meta:
        app_label = 'mimikry'
        ordering = ['name']
        # add view permission (GET)
        permissions = (
            ("view_osprofile", "Can view avaliable osprofiles"),
            )
