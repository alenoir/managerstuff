# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Url'
        db.create_table(u'bot_url', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'bot', ['Url'])

        # Adding model 'BotUrl'
        db.create_table(u'bot_boturl', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bot', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bot.Bot'])),
            ('url', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bot.Url'])),
            ('action', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bot.Action'])),
        ))
        db.send_create_signal(u'bot', ['BotUrl'])


    def backwards(self, orm):
        # Deleting model 'Url'
        db.delete_table(u'bot_url')

        # Deleting model 'BotUrl'
        db.delete_table(u'bot_boturl')


    models = {
        u'bot.action': {
            'Meta': {'object_name': 'Action'},
            'function': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bot.Service']"})
        },
        u'bot.bot': {
            'Meta': {'object_name': 'Bot'},
            'actions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bot.Action']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bots'", 'to': u"orm['bot.Service']"}),
            'url_rss': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'urls': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'bots'", 'symmetrical': 'False', 'through': u"orm['bot.BotUrl']", 'to': u"orm['bot.Url']"})
        },
        u'bot.boturl': {
            'Meta': {'object_name': 'BotUrl'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bot.Action']"}),
            'bot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bot.Bot']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bot.Url']"})
        },
        u'bot.service': {
            'Meta': {'object_name': 'Service'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'bot.url': {
            'Meta': {'object_name': 'Url'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['bot']