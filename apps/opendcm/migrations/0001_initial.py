# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SystemGroup'
        db.create_table('opendcm_systemgroup', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=4096, blank=True)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['opendcm.SystemGroup'])),
        ))
        db.send_create_signal('opendcm', ['SystemGroup'])

        # Adding model 'NextBoot'
        db.create_table('opendcm_nextboot', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('kernel', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('template', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('initrd', self.gf('django.db.models.fields.CharField')(max_length=200, blank=True)),
            ('cmdline', self.gf('django.db.models.fields.CharField')(max_length=8096, blank=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=4096, blank=True)),
        ))
        db.send_create_signal('opendcm', ['NextBoot'])

        # Adding model 'DataCenter'
        db.create_table('opendcm_datacenter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=4096, blank=True)),
        ))
        db.send_create_signal('opendcm', ['DataCenter'])

        # Adding model 'Floor'
        db.create_table('opendcm_floor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('datacenter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.DataCenter'])),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=4096, blank=True)),
        ))
        db.send_create_signal('opendcm', ['Floor'])

        # Adding model 'Room'
        db.create_table('opendcm_room', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('floor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.Floor'])),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=4096, blank=True)),
        ))
        db.send_create_signal('opendcm', ['Room'])

        # Adding model 'Row'
        db.create_table('opendcm_row', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('room', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.Room'])),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=4096, blank=True)),
        ))
        db.send_create_signal('opendcm', ['Row'])

        # Adding model 'Rack'
        db.create_table('opendcm_rack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('row', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.Row'])),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=42)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=4096, blank=True)),
        ))
        db.send_create_signal('opendcm', ['Rack'])

        # Adding model 'System'
        db.create_table('opendcm_system', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('system_group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.SystemGroup'])),
            ('rack', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.Rack'])),
            ('height', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('next_boot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.NextBoot'])),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=4096, blank=True)),
        ))
        db.send_create_signal('opendcm', ['System'])

        # Adding model 'Bios'
        db.create_table('opendcm_bios', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('biosdate', self.gf('django.db.models.fields.DateTimeField')()),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ssn', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('manufacturer', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.System'])),
        ))
        db.send_create_signal('opendcm', ['Bios'])

        # Adding model 'EthernetCard'
        db.create_table('opendcm_ethernetcard', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('speed', self.gf('django.db.models.fields.IntegerField')(default=1000)),
            ('mac', self.gf('django.db.models.fields.CharField')(max_length=17)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.System'])),
        ))
        db.send_create_signal('opendcm', ['EthernetCard'])

        # Adding model 'HardDrive'
        db.create_table('opendcm_harddrive', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('devname', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.System'])),
        ))
        db.send_create_signal('opendcm', ['HardDrive'])

        # Adding model 'Mainboard'
        db.create_table('opendcm_mainboard', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('architecture', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('product', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('memorysize', self.gf('django.db.models.fields.IntegerField')()),
            ('processorcount', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('maximummemory', self.gf('django.db.models.fields.IntegerField')()),
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.System'])),
        ))
        db.send_create_signal('opendcm', ['Mainboard'])

        # Adding model 'MemoryDimm'
        db.create_table('opendcm_memorydimm', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('bank', self.gf('django.db.models.fields.IntegerField')()),
            ('serialnumber', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('speed', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.System'])),
        ))
        db.send_create_signal('opendcm', ['MemoryDimm'])

        # Adding model 'Processor'
        db.create_table('opendcm_processor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('modelname', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('flags', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('mhz', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('cache', self.gf('django.db.models.fields.IntegerField')()),
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.System'])),
        ))
        db.send_create_signal('opendcm', ['Processor'])

        # Adding model 'SoundCard'
        db.create_table('opendcm_soundcard', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.System'])),
        ))
        db.send_create_signal('opendcm', ['SoundCard'])

        # Adding model 'VideoCard'
        db.create_table('opendcm_videocard', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('product', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.System'])),
        ))
        db.send_create_signal('opendcm', ['VideoCard'])

        # Adding model 'Event'
        db.create_table('opendcm_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('descr', self.gf('django.db.models.fields.CharField')(max_length=4096, blank=True)),
            ('eventtype', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['opendcm.System'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('opendcm', ['Event'])


    def backwards(self, orm):
        # Deleting model 'SystemGroup'
        db.delete_table('opendcm_systemgroup')

        # Deleting model 'NextBoot'
        db.delete_table('opendcm_nextboot')

        # Deleting model 'DataCenter'
        db.delete_table('opendcm_datacenter')

        # Deleting model 'Floor'
        db.delete_table('opendcm_floor')

        # Deleting model 'Room'
        db.delete_table('opendcm_room')

        # Deleting model 'Row'
        db.delete_table('opendcm_row')

        # Deleting model 'Rack'
        db.delete_table('opendcm_rack')

        # Deleting model 'System'
        db.delete_table('opendcm_system')

        # Deleting model 'Bios'
        db.delete_table('opendcm_bios')

        # Deleting model 'EthernetCard'
        db.delete_table('opendcm_ethernetcard')

        # Deleting model 'HardDrive'
        db.delete_table('opendcm_harddrive')

        # Deleting model 'Mainboard'
        db.delete_table('opendcm_mainboard')

        # Deleting model 'MemoryDimm'
        db.delete_table('opendcm_memorydimm')

        # Deleting model 'Processor'
        db.delete_table('opendcm_processor')

        # Deleting model 'SoundCard'
        db.delete_table('opendcm_soundcard')

        # Deleting model 'VideoCard'
        db.delete_table('opendcm_videocard')

        # Deleting model 'Event'
        db.delete_table('opendcm_event')


    models = {
        'opendcm.bios': {
            'Meta': {'object_name': 'Bios'},
            'biosdate': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'manufacturer': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'ssn': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.System']"}),
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
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.System']"}),
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
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.System']"}),
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
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.System']"}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'opendcm.memorydimm': {
            'Meta': {'object_name': 'MemoryDimm'},
            'bank': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'serialnumber': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'speed': ('django.db.models.fields.IntegerField', [], {}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.System']"}),
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
        'opendcm.processor': {
            'Meta': {'object_name': 'Processor'},
            'cache': ('django.db.models.fields.IntegerField', [], {}),
            'flags': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mhz': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modelname': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.System']"}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.System']"})
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
            'system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['opendcm.System']"})
        }
    }

    complete_apps = ['opendcm']