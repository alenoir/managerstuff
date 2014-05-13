import feedparser
from django.db import models
from libs.stumbleupon.functions import *
from selenium import webdriver

class Service(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Action(models.Model):
    service = models.ForeignKey(Service)
    name = models.CharField(max_length=255)
    function = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class Url(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.link

class Rss(models.Model):
    link = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.link

class Bot(models.Model):
    service = models.ForeignKey(Service, related_name='bots')
    name = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    actions = models.ManyToManyField(Action)
    rss = models.ManyToManyField(Rss)
    urls = models.ManyToManyField(Url, related_name='bots', through='BotUrl')

    def __unicode__(self):
        return self.name

    def runActions(self):
        chromeOptions = webdriver.ChromeOptions()
        driver = webdriver.Chrome(chrome_options=chromeOptions)

        loginStumble(driver, self.login, self.password)

        for action in self.actions.all():
            try:
                for rss in self.rss.all():
                    print 'parse rss : ' + rss.title
                    feed = feedparser.parse(rss.link)
                    count = 0
                    for entry in feed['entries']:
                        url, createdUrl = Url.objects.get_or_create(link = entry['link'], title = entry['title'])
                        botUrl, created = BotUrl.objects.get_or_create(bot = self, url = url, action = action)
                        if created:
                            likePage(driver, url.link)
                            count+=1
                        if count >=10:
                            break

            except Exception, e:
                print e

        driver.close()
        driver.quit

class BotUrl(models.Model):
    bot = models.ForeignKey(Bot)
    url = models.ForeignKey(Url)
    action = models.ForeignKey(Action)
    created_at = models.DateTimeField(auto_now_add=True)
