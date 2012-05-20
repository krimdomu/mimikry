from django.db import models
from django.conf import settings
from opendcm.models.hardware import System
from opendcm.models.hardware import EthernetCard

class Profile(models.Model):
    lang = models.CharField(max_length=100)
    keyboard = models.CharField(max_length=100)
    selinux = models.BooleanField()
    firewall = models.BooleanField()
    timezone = models.CharField(max_length=100)
    boot_device = models.OneToOneField(EthernetCard, null=True, related_name='ethernetcard')

    system = models.OneToOneField(System, related_name='profile')
   
    def __unicode__(self):
        return u'Profile of %s' % (self.system.name)
   
    class Meta:
        app_label = 'opendcm'
        # add view permission (GET)
        permissions = (
            ("view_Profile", "Can view avaliable profiles"),
            )
   
