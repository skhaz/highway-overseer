# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from crawler.items import Entry
from crawler.loaders import EntryLoader


class RegisSpider(CrawlSpider):
    name = 'regis'
    allowed_domains = ['autopistaregis.com.br']
    start_urls = ['http://www.autopistaregis.com.br/?link=noticias.todas']
    rules = (
        Rule(LinkExtractor(allow=r'\?link=noticias.?ver*'), callback='parse_news'),
    )

    def parse_news(self, response):
        loader = EntryLoader(item=Entry(), response=response)
        loader.add_xpath('content', '//*[@id="noticia"]/p[not(position() > last() -3)]//text()')
        return loader.load_item()
