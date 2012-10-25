# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AVS'
        db.create_table('freenas_avs', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('enable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('freenas', ['AVS'])


    def backwards(self, orm):
        # Deleting model 'AVS'
        db.delete_table('freenas_avs')


    models = {
        'freenas.avs': {
            'Meta': {'object_name': 'AVS'},
            'enable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['freenas']
