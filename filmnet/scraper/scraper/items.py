# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class YourItem(scrapy.Item):
    title = scrapy.Field()
    release_year = scrapy.Field()
    summary = scrapy.Field()
    rate = scrapy.Field()
    duration = scrapy.Field()
    genres = scrapy.Field()
    link = scrapy.Field()
    actors = scrapy.Field()
    image_urls = scrapy.Field()
