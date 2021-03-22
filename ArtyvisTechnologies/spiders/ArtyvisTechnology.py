import scrapy
from scrapy import Request
from urllib.parse import urljoin


class ArtyvistechnologySpider(scrapy.Spider):
    name = 'ArtyvisTechnology'
    allowed_domains = ['www.houseofindya.com']
    start_urls = ['http://www.houseofindya.com/zyra/cat?label=Jewelry/']

    def parse(self, response):
        necklace_set = response.xpath(
            '//*[@id="wrapper"]/div[3]/div[1]/div[2]/div[1]/div[1]/div[4]/div/ul/li/a/@href').getall()
        for url in necklace_set:
            yield Request(urljoin(response.url, url), callback=self.parse_list)

    def parse_list(self, response):
        d = []
        for info in response.xpath('//*[@id="wrapper"]/div[3]/div[1]/div[2]/div[2]/div[5]/ul/li'):
            d.append({
                'image': info.xpath('.//a/div[1]/img/@data-original').extract()[0],
                'desc': info.xpath('.//a/div[2]/p/text()').get(),
                'price': info.xpath('.//a/div[3]/span[1]/text()').get()
            })
        yield {
            response.url.split('/')[5]: d
        }

# Command to run
# scrapy crawl ArtyvisTechnology -o data.json
# python json_to_csv.py