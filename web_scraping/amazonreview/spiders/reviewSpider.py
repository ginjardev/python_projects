import scrapy
from amazonreview.items import AmazonreviewItem

class ReviewspiderSpider(scrapy.Spider):
    name = 'reviewSpider'
    allowed_domains = ['amazon.com']
    start_urls = [
        'https://www.amazon.com/48-Laws-Power-Robert-Greene/dp/0140280197/ref=sr_1_1?keywords=48+laws+of+power&qid=1673536586&sr=8-1'
        ]

    def parse(self, response):
        all_reviews = response.xpath('//div[@data-hook="reviews-medley-footer"]//a[@data-hook="see-all-reviews-link-foot"]/@href').extract_first()
        yield response.follow("https://www.amazon.com"+all_reviews, callback=self.parse_page)

    def parse_page(self, response):
        name =response.xpath('//div[@data-hook="review"]//span[@class="a-profile-name"]/text()').extract()
        reviewerLink=response.xpath('//div[@data-hook="review"]//a[@class="a-profile"]/@href').extract()
        reviewTitles=response.xpath('//a[@data-hook="review-title"]/span/text()').extract()
        reviewBody=response.xpath('//span[@data-hook="review-body"]/span').xpath('normalize-space()').getall()
        verifiedPurchase=response.xpath('//span[@data-hook="avp-badge"]/text()').extract()
        postDate=response.xpath('//span[@data-hook="review-date"]/text()').extract()
        starRating=response.xpath('//i[@data-hook="review-star-rating"]/span[@class="a-icon-alt"]/text()').extract()
        helpful = response.xpath('//span[@class="cr-vote"]//span[@data-hook="helpful-vote-statement"]/text()').extract()

        for (name, reviewLink, title, Review, Verified, date, rating, helpful_count) \
            in zip(name, reviewerLink, reviewTitles, reviewBody, verifiedPurchase, postDate, starRating, helpful):
      
    #   # Getting the Next Page URL for futher scraping.
            next_urls = response.css('.a-last > a::attr(href)').extract_first()
      
        yield AmazonreviewItem(name=name, reviewerLink = reviewLink, reviewTitles=title, reviewBody=Review, \
            verifiedPurchase=Verified, postDate=date, starRating=rating, helpful=helpful_count, nextPage=next_urls)

        next_page = response.css('.a-last > a::attr(href)').extract_first()
  # Checking if next page is not none then loop back in the same function with the next page URL.
        if next_page is not None:
            yield response.follow("https://www.amazon.com"+next_page, callback=self.parse_page)
