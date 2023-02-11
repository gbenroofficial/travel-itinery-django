# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from dataclasses import field
import scrapy
from scrapy_djangoitem import DjangoItem
from eventProps.models import EventProp



class ScraperItem(DjangoItem):
    django_model = EventProp
    
