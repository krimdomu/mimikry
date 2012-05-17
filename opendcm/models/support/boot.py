from django.db import models
from django.conf import settings
                
class NextBoot(models.Model):
   name = models.CharField(max_length=100)
   descr = models.CharField(max_length=4096, blank=True)
   
   def __unicode__(self):
       return u'%s' % (self.name)
   
   class Meta:
       app_label = 'opendcm'
       # order ascending by order
       ordering = ['name']
       # add view permission (GET)
       permissions = (
           ("view_NextBoot", "Can view avaliable netboots"),
           )
   
