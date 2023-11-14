# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
# useful for handling different item types with a single interface

from movie.models import Movie
from asgiref.sync import sync_to_async


class ScrapyAppPipeline(object):
    @sync_to_async
    def save_to_database(self, item):
        instance = Movie(title=item['title'], release_year=item['release_year'], summary=item['summary'],
                         rate=item['rate'], duration=item['duration'], genres=item['genres'], link=item['link'],
                         actors=item['actors'])
        instance.save()

    async def process_item(self, item, spider):
        await self.save_to_database(item)
        return item


class ScraperPipeline:
    def process_item(self, item, spider):
        return item
