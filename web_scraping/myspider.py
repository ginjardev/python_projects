import scrapy

# class BlogSpider(scrapy.Spider):
#     name = 'blogsider'
#     start_urls = ['https://www.zyte.com/blog/']

#     def parse(self, response):
#         for title in response.css('.oxy-post-title'):
#             yield {'title': title.css('::text').get()}
        
#         for next_page in response.css('a.next'):
#             yield response.follow(next_page, self.parse)

# class Product(scrapy.Item):
#     product_url = scrapy.Field()
#     price = scrapy.Field()
#     title = scrapy.Field()
#     img_url = scrapy.Field()


# class EcomSpider(scrapy.Spider):
#     name = 'ecom_spider'
#     allowed_domains = ['clever-lichterman-044f16.netlify.app']
#     start_urls = ['https://clever-lichterman-044f16.netlify.app/products/taba-cream.1/']

#     def parse(self, response):
#         item = Product()
#         item['product_url'] = response.url
#         item['price'] = response.xpath("//div[@class='my-4']/span/text()").get()
#         item['title'] = response.xpath('//section[1]//h2/text()').get()
#         item['img_url'] = response.xpath("//div[@class='product-slider']//img/@src").get(0)
#         return item



class BookScraper(scrapy.Spider):
    name = "bsspider"
    allowed_urls = ["amazon.com"]
    start_urls = ['https://www.amazon.com/gp/browse.html?node=2649512011&ref_=nav_em__nav_desktop_sa_intl_movies_0_2_20_2']

    def parse(self, response):
        for title in response.xpath('//div[contains(@class, "octopus-pc-asin-title")]/span'):
            yield {'title':title}
