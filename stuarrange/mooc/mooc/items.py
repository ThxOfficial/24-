# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MoocItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    img = scrapy.Field()
    status=scrapy.Field()
    price=scrapy.Field()
    linque=scrapy.Field()

