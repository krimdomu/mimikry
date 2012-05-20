# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Profile'
        db.create_table('opendcm_profile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('lang', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('keyboard', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('selinux', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('firewall', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('timezone', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('system', self.gf('django.db.models.fields.related.OneToOneField')(related_name='profile', unique=True, to=orm['opendcm.System'])),
        ))
        db.send_create_signal('opendcm', ['Profile'])


    def backwards(self, orm):
        # Deleting model 'Profile'
        db.delete_table('opendcm_profile')


    models = {
        'opendcm.bios': {
            'Meta': {'object_name': 'Bios'},
            'biosdate': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'system': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'bios'", 'unique': 'True', 'to': "orm['opendcm.System']"}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'opendcm.datacenter': {
            'Meta': {'ordering': "['name']", 'object_name': 'DataCenter'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'opendcm.ethernetcard': {
            'Meta': {'object_name': 'EthernetCard'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mac': ('django.db.models.fields.CharField', [], {'max_length': '17'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'speed': ('django.db.models.fields.IntegerField', [], {'default': '1000'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ethernetcards'", 'to': "orm['opendcm.System']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'opendcm.event': {
            'Meta': {'ordering': "['name']", 'object_name': 'Event'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'blank': 'True'}),
            'eventtype': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.System']"})
        },
        'opendcm.floor': {
            'Meta': {'ordering': "['name']", 'object_name': 'Floor'},
            'datacenter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.DataCenter']"}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'opendcm.harddrive': {
            'Meta': {'object_name': 'HardDrive'},
            'devname': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'harddrives'", 'to': "orm['opendcm.System']"}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'opendcm.mainboard': {
            'Meta': {'object_name': 'Mainboard'},
            'architecture': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maximummemory': ('django.db.models.fields.IntegerField', [], {}),
            'memorysize': ('django.db.models.fields.IntegerField', [], {}),
            'processorcount': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'system': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'mainboard'", 'unique': 'True', 'to': "orm['opendcm.System']"}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'opendcm.memorydimm': {
            'Meta': {'object_name': 'MemoryDimm'},
            'bank': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'serialnumber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'speed': ('django.db.models.fields.IntegerField', [], {}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'memorydimms'", 'to': "orm['opendcm.System']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'opendcm.nextboot': {
            'Meta': {'ordering': "['name']", 'object_name': 'NextBoot'},
            'cmdline': ('django.db.models.fields.CharField', [], {'max_length': '8096', 'blank': 'True'}),
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initrd': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'kernel': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'template': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'opendcm.partition': {
            'Meta': {'object_name': 'Partition'},
            'fstype': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mountpoint': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ondisk': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'paritions'", 'to': "orm['opendcm.System']"})
        },
        'opendcm.processor': {
            'Meta': {'object_name': 'Processor'},
            'cache': ('django.db.models.fields.IntegerField', [], {}),
            'flags': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mhz': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modelname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'processors'", 'to': "orm['opendcm.System']"}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'opendcm.profile': {
            'Meta': {'object_name': 'Profile'},
            'firewall': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keyboard': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'selinux': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'system': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['opendcm.System']"}),
            'timezone': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'opendcm.rack': {
            'Meta': {'ordering': "['name']", 'object_name': 'Rack'},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '42'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'row': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.Row']"})
        },
        'opendcm.room': {
            'Meta': {'ordering': "['name']", 'object_name': 'Room'},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'blank': 'True'}),
            'floor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.Floor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'opendcm.row': {
            'Meta': {'ordering': "['name']", 'object_name': 'Row'},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'room': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.Room']"})
        },
        'opendcm.soundcard': {
            'Meta': {'object_name': 'SoundCard'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'soundcards'", 'to': "orm['opendcm.System']"})
        },
        'opendcm.system': {
            'Meta': {'ordering': "['name']", 'object_name': 'System'},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'next_boot': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.NextBoot']"}),
            'rack': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.Rack']"}),
            'system_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.SystemGroup']"})
        },
        'opendcm.systemgroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'SystemGroup'},
            'descr': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['opendcm.SystemGroup']"})
        },
        'opendcm.videocard': {
            'Meta': {'object_name': 'VideoCard'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'videocards'", 'to': "orm['opendcm.System']"})
        }
    }

    complete_apps = ['opendcm']