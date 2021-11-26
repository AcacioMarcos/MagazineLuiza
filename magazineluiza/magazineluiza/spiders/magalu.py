import scrapy


class MagaluSpider(scrapy.Spider):
    name = 'magalu'

    start_urls = [f'https://www.magazineluiza.com.br/selecao/ofertasdodia/?page={i}' for i in range(1,6)]

    def parse(self, response, **kwargs):
        for i in response.xpath('//li[@class="sc-kdneuM cNOGCg"]'):
            titulo = i.xpath('.//h2[@data-testid="product-title"]/text()').get()
            preco_antigo = i.xpath('.//p[@data-testid="price-original"]//text()').getall()
            preco_novo = i.xpath('.//p[@data-testid="price-value"]//text()').getall()
            link = i.xpath('./a/@href').get()

            yield {
                'titulo' : titulo,
                'preco_antigo' : preco_antigo,
                'preco_novo' : preco_novo,
                'link' : link
            }


