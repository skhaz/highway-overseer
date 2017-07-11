# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join


class EntryLoader(ItemLoader):
    content_in = MapCompose(unicode.strip)
    content_out = Join()
