# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonreviewItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    reviewerLink = scrapy.Field()
    reviewTitles = scrapy.Field()
    reviewBody = scrapy.Field()
    verifiedPurchase = scrapy.Field()
    postDate = scrapy.Field()
    starRating = scrapy.Field()
    helpful = scrapy.Field()
    nextPage = scrapy.Field(default = 'null')
