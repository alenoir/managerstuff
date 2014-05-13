# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'BotUrl.created_at'
        db.add_column(u'bot_boturl', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 5, 12, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'BotUrl.created_at'
        db.delete_column(u'bot_boturl', 'created_at')


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
            'rss': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['bot.Rss']", 'symmetrical': 'False'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'bots'", 'to': u"orm['bot.Service']"}),
            'urls': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'bots'", 'symmetrical': 'False', 'through': u"orm['bot.BotUrl']", 'to': u"orm['bot.Url']"})
        },
        u'bot.boturl': {
            'Meta': {'object_name': 'BotUrl'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bot.Action']"}),
            'bot': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bot.Bot']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bot.Url']"})
        },
        u'bot.rss': {
            'Meta': {'object_name': 'Rss'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
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