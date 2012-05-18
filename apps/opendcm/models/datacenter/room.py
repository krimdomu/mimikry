from django.db import models
from django.conf import settings
from floor import Floor
                
class Room(models.Model):
   name = models.CharField(max_length=100)
   floor = models.ForeignKey(Floor)
   descr = models.CharField(max_length=4096, blank=True)
   
   def __unicode__(self):
       return u'%s-%s' % (self.name, self.floor)
   
   class Meta:
       app_label = 'opendcm'
       # order ascending by order
       ordering = ['name']
       # add view permission (GET)
       permissions = (
           ("view_room", "Can view avaliable rooms"),
           )
   
