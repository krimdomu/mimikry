from django.db import models
from django.conf import settings
                
class Location(models.Model):
    name = models.CharField(max_length=100)
    street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)    
    order = models.IntegerField(unique=True, default=0)
    def save(self, *args, **kwargs):
        # autogenerate order id if none is provided
        if self.order == 0:
            query_result = Location.objects.all()
            if query_result:
                self.order = query_result.aggregate(max_value=models.Max('order'))['max_value'] + 1
            else:
                self.order = 1
        super(Location, self).save(*args, **kwargs)
            
    def __unicode__(self):
        return u'%d-%s' % (self.order, self.name)
        
    class Meta:
        app_label = 'mimikry'
        # order ascending by order
        ordering = ['order']
        # add view permission (GET)
        permissions = (
            ("view_location", "Can view avaliable locations"),
            )
