# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class NaverblogPipeline(object):
    
    def process_item(self, item, spider):        
        if(item['date'].find('2015-01-14')!=-1):
            return item
        else:
            raise DropItem(item)
