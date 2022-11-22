import scrapy
from scrapy import Selector


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [f'https://quotes.toscrape.com/page/{i}/' for i in range(20)]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        spans = response.css('div.quote')
        for span in spans:
            yield {
                'author': span.css('small.author::text').get(),
                'text': span.css('span.text::text').get(),
                'tags': span.css('a.tag::text').getall(),
            }


        # page = response.url.split("/")[-2]
        # filename = f'quotes-{page}.html'
        # with open(filename, 'wb') as file:
        #     file.write(response.body)
        # self.log(f'Saved file {filename}')

