from urllib.parse import urljoin

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import YourItem


class MovieSpider(scrapy.Spider):
    name = 'movies'
    start_urls = ['https://filmnet.ir/contents?types=single_video']

    def parse(self, response):
        for i in range(100):
            title = response.xpath((f"/html/body/div/main/div[2]/section[2]/div/div/ul/li[{i}]/div/div/text()")).getall()
            if title:
                item = YourItem()
                image_urls = response.xpath(f'/html/body/div/main/div[2]/section[2]/div/div/ul/li[{i}]/div/a/img/@src').get()
                item['image_urls'] = [image_urls]
                item['title'] = title[0]
                detail = response.xpath((f"/html/body/div/main/div[2]/section[2]/div/div/ul/li[{i}]/div/a/@href")).get()
                detail_page_url_absolute = urljoin(response.url, detail)
                item['link'] = detail_page_url_absolute
                yield scrapy.Request(url=detail_page_url_absolute, callback=self.parse_detail, meta={'item': item})

    def parse_detail(self, response):
        item = response.meta['item']
        release_year = response.xpath('/html/body/div/main/section/div[2]/ul[2]/li[1]/div/div/span/text()').get()
        summary = response.xpath('//p[@class="eh50r6x0 css-1bes4v e1eum8tf0"]/text()').get()
        rate = response.xpath('//span[@class="css-70wr7 e1344cf00"]/text()').get()
        duration = response.xpath('/html/body/div/main/section/div[2]/ul[2]/li[1]/div/span/span[2]/text()').get()
        genres = response.xpath('/html/body/div/main/section/div[2]/ul[3]/li[1]/a/text()').get()
        actors = response.xpath('/html/body/div/main/section/div[2]/table/tbody/tr[2]/td[2]/text()').get()
        item['release_year'] = release_year
        item['summary'] = summary
        item['rate'] = rate
        item['duration'] = duration
        item['genres'] = genres
        item['actors'] = actors

        yield item
