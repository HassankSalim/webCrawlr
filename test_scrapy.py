import scrapy
import re
from scrapy.crawler import CrawlerProcess

class TechCrunchSpider(scrapy.Spider):
	name = "TechSpider"
	start_urls = ['https://techcrunch.com/2017/12/13/nasty-gal-founder-sophia-amoruso-just-raised-venture-funding-for-her-new-company/']

	some_tag = '<\w+[^>]*>(.*?)</\w+>'
	close_p_tag = '</p>'
	open_p_tag = '<p[^>]*>'

	def parse(self, response):
		div_contents = response.css(r'div.article-entry')
		result = ""
		for i in div_contents.css('p').extract():
			no_p_tag = re.sub('%s|%s'%(self.close_p_tag, self.open_p_tag), '', i)
			result += ''.join(re.split(self.some_tag, no_p_tag)) + '\n '
		return { 'result':result }


if __name__ == '__main__':
	
	test = 'https://techcrunch.com/2017/12/11/max-levchins-affirm-raised-200-million-at-nearly-2-billion-valuation/'
	process = CrawlerProcess({ 'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)' })
	process.crawl(TechCrunchSpider, start_urls=[test, ])
	process.crawl(TechCrunchSpider)
	process.start()
