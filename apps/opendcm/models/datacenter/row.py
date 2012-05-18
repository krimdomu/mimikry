from django.db import models
from django.conf import settings
from room import Room
                
class Row(models.Model):
   name = models.CharField(max_length=100)
   room = models.ForeignKey(Room)
   descr = models.CharField(max_length=4096, blank=True)
   
   def __unicode__(self):
       return u'%s-%s' % (self.name, self.room)
   
   class Meta:
       app_label = 'opendcm'
       # order ascending by order
       ordering = ['name']
       # add view permission (GET)
       permissions = (
           ("view_row", "Can view avaliable rows"),
           )
   
