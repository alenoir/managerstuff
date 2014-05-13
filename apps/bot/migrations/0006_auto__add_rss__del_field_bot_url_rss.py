# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Rss'
        db.create_table(u'bot_rss', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'bot', ['Rss'])

        # Deleting field 'Bot.url_rss'
        db.delete_column(u'bot_bot', 'url_rss')

        # Adding M2M table for field rss on 'Bot'
        m2m_table_name = db.shorten_name(u'bot_bot_rss')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('bot', models.ForeignKey(orm[u'bot.bot'], null=False)),
            ('rss', models.ForeignKey(orm[u'bot.rss'], null=False))
        ))
        db.create_unique(m2m_table_name, ['bot_id', 'rss_id'])


    def backwards(self, orm):
        # Deleting model 'Rss'
        db.delete_table(u'bot_rss')

        # Adding field 'Bot.url_rss'
        db.add_column(u'bot_bot', 'url_rss',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Removing M2M table for field rss on 'Bot'
        db.delete_table(db.shorten_name(u'bot_bot_rss'))


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