import scrapy

from ..items import MoocItem


class MoocgetSpider(scrapy.Spider):
    name = "moocget"
    allowed_domains = ["coding.imooc.com"]
    start_urls = ["https://coding.imooc.com/"]

    def parse(self, response):
        whh = response.xpath('//ul[@class="course-list clearfix"]/li/a')
        for i in whh:
            name = i.xpath('./p[1]/text()').extract()
            img = i.xpath('./div/@style').extract()
            sta=i.xpath('./p[2]/span[1]/text()').extract()
            pri=i.xpath('./p[3]/span[1]/text()').extract()
            lin=i.xpath('./@href').extract()
            for a in img:
                src = 'http:' + a[22:-1]
                print(name)
            for b in lin:
                linky='https://coding.imooc.com'+b

                data = MoocItem(name=name, img=src,status=sta,price=pri,linque=linky)
                yield data

