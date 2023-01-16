# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonMovieDetail(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    summary = scrapy.Field()
    runtime = scrapy.Field()
    release_year = scrapy.Field()
    rating = scrapy.Field()
    buy_price = scrapy.Field()