# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class WaiguoPipeline(object):
#     def process_item(self, item, spider):
#         return item

import json
class WaiguoPipeline(object):
    # 打开文件
    def open_spider(self,spider):
        self.fp = open('妹子图.txt','w',encoding='utf8')

    def process_item(self, item, spider):
        dic = dict(item)
        string = json.dumps(dic,ensure_ascii=False)
        self.fp.write(string + '\n')
        # return item
    # 关闭文件
    def close_spider(self,spider):
        self.fp.close()