from django.contrib import admin
from .models import *

admin.site.register(Service)
admin.site.register(Action)
admin.site.register(Bot)
admin.site.register(Url)
admin.site.register(BotUrl)
admin.site.register(Rss)

