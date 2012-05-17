from django.db import models
from django.conf import settings
from row import Row
                
class Rack(models.Model):
   name = models.CharField(max_length=100)
   row = models.ForeignKey(Row)
   height = models.IntegerField(default=42)    
   def __unicode__(self):
       return u'%s-%s' % (self.name, self.row)
        
   class Meta:
       app_label = 'opendcm'
       # order ascending by order
       ordering = ['name']
       # add view permission (GET)
       permissions = (
           ("view_racks", "Can view avaliable racks"),
           )
