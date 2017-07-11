# -*- coding: utf-8 -*-
from scrapy import Item, Field


class Entry(Item):
    uid = Field()
    spider = Field()
    timestamp = Field()
    content = Field()
