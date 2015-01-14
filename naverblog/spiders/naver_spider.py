# -*- coding: utf-8 -*-

import scrapy

from naverblog.items import NaverblogItem


class NaverblogSpider(scrapy.Spider):        
	name="naver"
	allowed_domains = ["blog.naver.com"]
	start_urls = ["http://section.blog.naver.com/sub/PostListByDirectory.nhn?option.page.currentPage=%d&option.templateKind=0&option.directorySeq=%d&option.viewType=default&option.orderBy=date&option.latestOnly=0" % (p, s)
                      for s in xrange(5,36) for p in xrange(1,101)]

	def parse(self, response):                
		for sel in response.xpath('//ul[@class="list_type_1"]/li'):
                        item = NaverblogItem()
                        item['crawlUrl'] = response.url
                        item['title'] = sel.xpath('h5/a/text()').extract()[0]
                        item['category'] = response.xpath('//div[@class="sub_spot"]/h3/strong/text()').extract()[0]
                        item['link'] = sel.xpath('h5/a/@href').extract()[0]
                        item['date'] = sel.xpath('div[@class="list_data"]/span/text()').extract()[0].replace('.', '-')
                        if sel.xpath('div[@class="list_content"]/div/a/text()').extract() != []:
                                item['desc'] = sel.xpath('div[@class="list_content"]/div/a/text()').extract()[-1]
                        else :
                                item['desc'] = 'None'
                        if sel.xpath('div[@class="list_content"]/div[@class="multi_img"]/img/@src').extract() != []:
                                item['img'] = sel.xpath('div[@class="list_content"]/div[@class="multi_img"]/img/@src').extract()[0]
                        else :
                                item['img'] = 'None'
                                
                        yield item            
		
