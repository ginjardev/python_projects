import scrapy
from booksscraper.items import BooksscraperItem

class BspiderSpider(scrapy.Spider):
    name = 'bspider'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?bbn=2649512011&rh=n%3A2649512011%2Cp_n_theme_browse-bin%3A2650366011&dc&qid=1673642373&rnid=2650362011&ref=lp_2649512011_nr_p_n_theme_browse-bin_1']

    def parse(self, response):
        names = response.css('span.a-size-medium.a-color-base.a-text-normal::text').extract()
        years = response.css('span.a-size-base.a-color-secondary.a-text-normal::text').extract()
        ratings = response.css('span.a-icon-alt::text').extract()
        prices = response.css('span.a-offscreen::text').extract()

        for (name, year, rating, price) in zip(names, years, ratings, prices): 
            yield BooksscraperItem(name= name, year= year, rating = rating, price=price)