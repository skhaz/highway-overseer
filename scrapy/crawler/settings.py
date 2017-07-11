# -*- coding: utf-8 -*-

BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'

SPIDER_MIDDLEWARES = {
    'scrapy_magicfields.MagicFieldsMiddleware': 100,
}

MAGIC_FIELDS = {
    'uid': "$response:url,r'id=(\d+)'",
    'spider': '$spider:name',
    'timestamp': "$time",
}

ITEM_PIPELINES = {
    'crawler.scrapy_firebase.FirebasePipeline': 900
}

FIREBASE_DATABASE = ''
FIREBASE_REF = ''
FIREBASE_SECRETS = """
"""
