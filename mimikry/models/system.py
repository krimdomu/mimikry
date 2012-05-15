from django.db import models
from django.conf import settings
from extensions.django.macaddress.fields import MACAddressField
from uuidfield import UUIDField

from mimikry.models import Cabinet
from mimikry.models import OSProfile


class System(models.Model):
    SYSTEM_STATUS = (
        (0, 'discovered'),
        (1, 'analysed'),
        (3, 'commisioning'),
        (4, 'installed'),
        (5, 'deactivated'),
        (6, 'unknown'),
    )
    BOOT_STATUS = (
        (0, 'ignore'),
        (1, 'analyse'),
        (2, 'commision'),
        (3, 'rescue'),
    )
    def get_default_cabinet():
        return Cabinet.objects.get(name='unknown')
    
    def get_default_osprofile():
        return OSProfile.objects.get(name='unknown')
                    
    cabinet = models.ForeignKey('Cabinet', related_name='systems', default=get_default_cabinet)
    osprofile = models.ForeignKey('OSProfile', related_name='systems', default=get_default_osprofile)
    name = models.CharField(max_length=100, default='unknown', null=True)
    description = models.CharField(max_length=4096, blank=True, null=True)
    mac_address = MACAddressField(unique=True)
    uuid = UUIDField(blank=True, null=True)
    system_status = models.IntegerField(choices=SYSTEM_STATUS, default=6, null=True)
    boot_status = models.IntegerField(choices=BOOT_STATUS, default=0, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'Servername: %s Rack: %s Boot Status: %s System Status: %s' % (
            self.name, self.cabinet, self.BOOT_STATUS[self.boot_status][1], self.SYSTEM_STATUS[self.boot_status][1] )

    class Meta:
        app_label = 'mimikry'
        # order by product_type and cabinet (desc)
        ordering = ['name', 'cabinet']
        # add view permission (GET)
        permissions = (
            ("view_system", "Can view avaliable systems"),
            )
