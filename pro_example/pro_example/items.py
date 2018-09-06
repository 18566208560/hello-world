# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Spider01Item(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()
    gender = scrapy.Field()


class LuhanItem(scrapy.Item):
    save_filed = ["msg_title","fans_name","fans_gender","fans_age","fans_star","fans_nation"]

    msg_title = scrapy.Field()
    msg_url = scrapy.Field()
    msg_id = scrapy.Field()
    msg_serial = scrapy.Field()


    fans_id = scrapy.Field()
    fans_name = scrapy.Field()
    fans_com = scrapy.Field()
    fans_serial = scrapy.Field()

    fans_gender = scrapy.Field()
    fans_age = scrapy.Field()
    fans_star = scrapy.Field()
    fans_nation = scrapy.Field()

    fans_0 = scrapy.Field()
    fans_1 = scrapy.Field()
