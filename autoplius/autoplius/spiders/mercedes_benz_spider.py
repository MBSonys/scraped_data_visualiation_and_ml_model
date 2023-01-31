import scrapy

class MercedesBenzSpider(scrapy.Spider):
    name = "mercedes_benz_c_class"
    start_urls = ['https://autoplius.lt/skelbimai/naudoti-automobiliai?make_id=67&model_id=685']


    def parse(self, response):
        for car in response.css('div.announcement-body'):
            yield {
                'name': car.css('div.announcement-title::text').get(),
                'price': car.css('div.announcement-pricing-info::text').get()
            }
