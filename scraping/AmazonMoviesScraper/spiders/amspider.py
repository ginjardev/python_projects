import scrapy
from AmazonMoviesScraper.items import AmazonMovieDetail

class AmspiderSpider(scrapy.Spider):
    name = 'amspider'
    allowed_domains = ['amazon.com']
    start_urls = [
        "https://amzn.to/3XfgcyH"
    ]

    def parse(self, response):
        links = response.css('a.a-link-normal.s-no-outline::attr(href)').extract()
        for link in links:
            link = 'https://www.amazon.com' + link
            yield response.follow(link, callback=self.parse_details)

        next_link = response.css('span.s-pagination-strip a::attr(href)').extract()
        next_link = next_link[-1]
        next_page_url = "https://www.amazon.com" + next_link
        yield response.follow(next_page_url, callback=self.parse)

    
    def parse_details(self, response):
        name = response.css('h1._2IIDsE._2sL6wP::text').extract_first()
        description = response.css('div._3qsVvm._1wxob_ > div::text').extract_first()
        year = response.css('span.XqYSS8:nth-of-type(3) > span::text').extract_first()
        rating = response.css('span.FDDgZI > span::text').extract_first()
        prices = response.css('button.SPqQmU._3RF4FN._1D7HW3._2G6lpB.tvod-button.av-button > span::text').extract()
        buy_price = prices[3]

        yield AmazonMovieDetail(name = name, description = description, year = year, rating = rating, price=buy_price)
