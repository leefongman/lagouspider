# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GoubanjiaPipeline(object):

    def open_spider(self, spider):
        self.f = open('proxy.dat', 'w')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        self.f.write(item['proxy'])
        self.f.flush()
        return item