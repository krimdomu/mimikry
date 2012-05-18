from django.db import models
from django.conf import settings
from dc import DataCenter
                
class Floor(models.Model):
   name = models.CharField(max_length=100)
   datacenter = models.ForeignKey(DataCenter)
   descr = models.CharField(max_length=4096, blank=True)
   
   def __unicode__(self):
       return u'%s-%s' % (self.name, self.datacenter)
   
   class Meta:
       app_label = 'opendcm'
       # order ascending by order
       ordering = ['name']
       # add view permission (GET)
       permissions = (
           ("view_floor", "Can view avaliable floors"),
           )
   
