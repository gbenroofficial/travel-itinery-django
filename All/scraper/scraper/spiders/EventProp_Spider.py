

from scrapy.spiders import CrawlSpider
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst
import scrapy

from scraper.scraper.items import ScraperItem

class EpCrawlSpider(CrawlSpider):
    name = "event_prop"
    start_urls = ["https://www.eventbrite.co.uk/d/united-states/all-events/"]
    allowed_domains = ['eventbrite.com',  'eventbrite.ca']
    rules = ( 
        Rule(
            LinkExtractor(allow="/d/united-kingdom/all-events/"),
            callback=None,
            follow=False,
        ),

        Rule(
            LinkExtractor(allow="/e/"),
            callback="parse_event",
            follow=False,
        ),
    )

    def parse_event(self, response):
        item = ScraperItem()
        for field in item.fields:
            item.setdefault(field, 'NULL')
        # item['price'] = response.css('listing-hero-footer hide-small hide-medium > div::text').get()
        item['name'] = response.css('listing-hero-title::text').get()

        
              
        item['image'] = response.css("#root > div > div > div.eds-structure__body > div > div > div > div.eds-fixed-bottom-bar-layout__content > div > main > div > div.event-details > div.hero-image-wrapper > div > picture > img::attr(src)").get()
       
       
       
       
       
       
        if item['name'] is not None and item['description'] is not None and item['image'] and item is not None:
            yield item
        pass
    


        if not item['name']:
            item['name'] = response.xpath('//*[@id="root"]/div/div[2]/div/div/div/div[1]/div/main/div/div[2]/div/div[1]/div/div[2]/div/div[2]/h1/text()').get()
        
        if not item['description']:
            item['description'] = response.xpath('//*[@id="root"]/div/div[2]/div/div/div/div[1]/div/main/div/div[2]/div/section[1]/div/div[2]/div[1]/p/strong/text()').get()
        
       
        if not item['name']:
            item['name'] = response.css('#root > div > div.eds-structure__body.eds-structure__body--overflow-set > div > div > div > div.eds-fixed-bottom-bar-layout__content > div > main > div > div.g-grid.g-grid--page-margin-manual > div > div.listing-hero-details__main-container.fx--fade-in.fx--delay-4 > div > div.g-cell.g-cell-1-1.g-cell--no-gutters.listing-hero__detailed-info.g-cell-lg-4-12 > div > div.listing-hero-body.listing-hero-body--parent > h1::text').get()
        
        if not item['description']:
            item['description'] = response.css('div.event-info__main > div > p > strong::text').get()
        

        if not item['name']:
            item['name'] = response.xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[2]/div/div[1]/div/div[2]/div/div[2]/h1/text()').get()
        
        if not item['description']:
            item['description'] = response.xpath('/html/body/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div/main/div/div[2]/div/section[1]/div/div[2]/div[1]/p/strong/text()').get()

        




