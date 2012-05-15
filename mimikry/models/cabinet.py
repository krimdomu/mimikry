from django.db import models
from django.conf import settings

class Cabinet(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey('Location', related_name='cabinets')
    description = models.CharField(max_length=4096, blank=True)            
    def __unicode__(self):
        return u'%s-%s' % (self.location, self.name)
        
    class Meta:
        app_label = 'mimikry'
        # order ascending by order
        ordering = ['name']
        # add view permission (GET)
        permissions = (
            ("view_cabinet", "Can view avaliable cabinets"),
            )
