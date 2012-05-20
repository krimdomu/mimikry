from django.db import models
from django.conf import settings
from opendcm.models.hardware import System

class SoundCard(models.Model):
   product = models.CharField(max_length=255)
   system = models.ForeignKey(System, related_name='soundcards')

   def __unicode__(self):
      return u'Soundcard of %s' % (self.system.name)

   class Meta:
      app_label = 'opendcm'
      permissions = (
         ("view_soundcard", "Can view available soundcards"),
         )
