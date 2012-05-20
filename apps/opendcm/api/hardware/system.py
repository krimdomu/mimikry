from tastypie import fields, utils
from tastypie.resources import ModelResource
from opendcm.models.hardware import System as SystemModel
from opendcm.api.support import NextBoot as NextBootResource
from opendcm.api.support import SystemGroup as SystemGroupResource

class System(ModelResource):
   next_boot = fields.ForeignKey(NextBootResource, 'next_boot', full=True)
   system_group = fields.ForeignKey(SystemGroupResource, 'system_group', full=True)
   bios = fields.ToOneField('opendcm.api.hardware.bios.Bios', 'bios', full=True)
   ethernetcards = fields.ToManyField('opendcm.api.hardware.ethernetcard.EthernetCard', 'ethernetcards', full=True, null=True)
   harddrives = fields.ToManyField('opendcm.api.hardware.harddrive.HardDrive', 'harddrives', full=True)
   mainboard = fields.ToOneField('opendcm.api.hardware.mainboard.Mainboard', 'mainboard', full=True, null=True)
   memorydimms = fields.ToManyField('opendcm.api.hardware.memorydimm.MemoryDimm', 'memorydimms', full=True, null=True)
   processors = fields.ToManyField('opendcm.api.hardware.processor.Processor', 'processors', full=True, null=True)
   soundcards = fields.ToManyField('opendcm.api.hardware.soundcard.SoundCard', 'soundcards', full=True, null=True)
   videocards = fields.ToManyField('opendcm.api.hardware.videocards.VideoCard', 'videocards', full=True, null=True)
   disks = fields.ToManyField('opendcm.api.system.disk.Disk', 'disks', full=True, null=True)
   profile = fields.ToOneField('opendcm.api.system.profile.Profile', 'profile', full=True, null=True)

   class Meta:
      queryset = SystemModel.objects.all()
      allowed_methods = ['get']

