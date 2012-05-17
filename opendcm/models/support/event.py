from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from opendcm.models.hardware import System

                
class Event(models.Model):
   name = models.CharField(max_length=100)
   descr = models.CharField(max_length=4096, blank=True)
   eventtype = models.CharField(max_length=100)
   system = models.ForeignKey(System)
   date = models.DateTimeField(auto_now_add=True)
   
   def __unicode__(self):
       return u'%s %s %s %s: %s' % (self.date, self.system.system_group, self.system, self.eventtype, self.name)
   
   class Meta:
       app_label = 'opendcm'
       # order ascending by order
       ordering = ['name']
       # add view permission (GET)
       permissions = (
           ("view_event", "Can view avaliable events"),
           )
   
