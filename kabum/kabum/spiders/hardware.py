import scrapy


class HardwareSpider(scrapy.Spider):
    name = "hardware"
    start_urls = ["https://www.kabum.com.br/hardware"]

    def parse(self, response):
        for item in response.xpath('//div[@class="sc-6ac6cf23-7 bvvvxW productCard"]'):
            yield {
                'nome': item.css('.nameCard::text').get(),
                'preço': item.css('.priceCard::text').get(),
            }

        prox_pag = response.xpath(
            '//a[contains(@class, "nextLink")]/@href').get()
        if prox_pag is not None:
            yield response.follow(prox_pag, callback=self.parse)
