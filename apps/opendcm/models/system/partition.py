from django.db import models
from django.conf import settings
from opendcm.models.system import Disk
                
class Partition(models.Model):
    mountpoint = models.CharField(max_length=200, null=True, blank=True)
    fstype = models.CharField(max_length=50, null=True, blank=True)
    ondisk = models.CharField(max_length=50)
    size = models.IntegerField()
    primary = models.BooleanField()
    disk = models.ForeignKey(Disk, null=True, related_name='partitions')
   
    def __unicode__(self):
        return u'Partition of %s (%s) on %s' % (self.disk.name, self.mountpoint, self.disk.system.name)
   
    class Meta:
        app_label = 'opendcm'
        # add view permission (GET)
        permissions = (
            ("view_Partition", "Can view avaliable partitions"),
            )
   
