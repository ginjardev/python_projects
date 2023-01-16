import scrapy
from booksscraper.items import BooksscraperItem


class BspiderSpider(scrapy.Spider):
    name = 'bspider'
    allowed_domains = ['amazon.com']    

    start_urls = [
        "https://amzn.to/3XfgcyH"
    ]

    def parse(self, response):
        links = response.css('a.a-link-normal.s-no-outline::attr(href)').extract()
        for link in links:
            link = 'https://www.amazon.com' + link
            # yield scrapy.Request(url=link, callback=self.parse_details)
            yield response.follow(link, callback=self.parse_details)

        next_page = response.css('span.s-pagination-strip a::attr(href)').extract()
        next_page = next_page[-1]
        nexturl = "https://www.amazon.com" + next_page
        # yield {'link': nexturl}
        yield response.follow(nexturl, callback=self.parse)

    def parse_details(self, response):
        name = response.css('h1._2IIDsE._2sL6wP::text').extract_first()
        description = response.css('div._3qsVvm._1wxob_ > div::text').extract_first()
        year = response.css('span.XqYSS8:nth-of-type(3) > span::text').extract_first()
        rating = response.css('span.FDDgZI > span::text').extract_first()
        price = response.css('button.SPqQmU._3RF4FN._1D7HW3._2G6lpB.tvod-button.av-button > span::text').extract()

        # next_page = response.css('span.s-pagination-strip a::attr(href)').extract()
        yield BooksscraperItem(name = name, description = description, year = year, rating = rating, price=price[3])

        # if next_page is not None: 
        #     next_page = next_page[-1]
        #     nexturl = "https://www.amazon.com" + next_page
        #     yield response.follow(nexturl, callback=self.parse)
           

        
        

    


