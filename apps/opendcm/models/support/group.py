from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
                
class SystemGroup(models.Model):
   name = models.CharField(max_length=100)
   descr = models.CharField(max_length=4096, blank=True)
   parent = models.ForeignKey("self", blank=True, null=True, related_name="children")
   
   def __unicode__(self):
       return u'%s' % (self.name)
   
   class Meta:
       app_label = 'opendcm'
       # order ascending by order
       ordering = ['name']
       # add view permission (GET)
       permissions = (
           ("view_SystemGroup", "Can view avaliable systemgroups"),
           )
   
