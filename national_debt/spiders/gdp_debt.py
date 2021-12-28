import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['worldpopulationreview.com']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        
        countries = response.xpath("//table/tbody/tr")
        
        for country in countries:
            yield {
                'country_name': country.xpath(".//td/a/text()").get(),
                #'country_link': country.xpath(".//td/a/@href").get(),
                'gdp_debt': country.xpath(".//td[2]/text()").get(),
                'population': country.xpath(".//td[3]/text()").get()
            }

 