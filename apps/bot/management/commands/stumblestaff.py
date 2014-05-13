from django.core.management.base import BaseCommand, CommandError
from apps.bot.models import *


class Command(BaseCommand):


    def handle(self, *args, **options):

        for service in Service.objects.filter(name="Stumbleupon"):
            for bot in service.bots.all():
                print 'Action for : ' + bot.name
                bot.runActions()
