# -*- coding: utf-8 -*-
import scrapy
import os
import random

# from ..items import WaiguoItem
# item = WaiguoItem()

class WgSpider(scrapy.Spider):
    name = 'wg'
    allowed_domains = []
    # start_urls = ['http://www.mmjpg.com/']
    start_urls = ['https://www.mzitu.com/search/%E9%99%86%E6%A2%93%E7%90%AA/']

    # 指定接着爬取的url
    # page = 1
    # url = 'http://www.mmjpg.com/home/{}'

    def parse(self, response):
        # urllist = response.xpath('//div[@class="pic"]//li/a/@href').extract()
        urllist = response.xpath('//div[@class="postlist"]//li/a/@href').extract()
        for url in urllist:
            # print(url)  http://www.mmjpg.com/mm/1393
            yield scrapy.Request(url=url, callback=self.download)

        # 接着发送请求，爬取其它页  在 for 循环的外面  ，和for同级
        # if self.page < 103:
        #     self.page += 1
        #     url = self.url.format(self.page)
        #     # 生成请求对象，扔给引擎
        #     # callback 就是处理响应的回调函数
        #     yield scrapy.Request(url=url, callback=self.parse)


    def download(self,response):
        # 最大页码
        # number = response.xpath('//div[ @ id = "page"]//*[last()-2]/text()').extract()
        number = response.xpath('//div[@class="pagenavi"]//*[last()-1]/span/text()').extract()
        nu = int(number[0])
        for num in range(1,nu + 1):
            xqurl = response.url + '/{}'.format(num)
            # print(xqurl)  http://www.mmjpg.com/mm/1534/1
            print(xqurl)
            print('正在下载第{}页'.format(xqurl))
            yield scrapy.Request(url=xqurl, callback=self.download_b)

        # # 接着发送请求，爬取其它页  在 for 循环的外面  ，和for同级
        # if self.content < int(number+1):
        #     pass
        # else:
        #     os.mkdir(content)
        #     url = self.url.format(self.page)
        #     # 生成请求对象，扔给引擎
        #     # callback 就是处理响应的回调函数
        #     yield scrapy.Request(url=url, callback=self.parse)



     # 详情页面
    def download_b(self,response):
        # 保存图片  保存名字  并且分类文件夹
        div = response.xpath('//div[@class="content"]/div[@class="main-image"]//a/img')
        img = div.xpath('@src').extract_first()
        title = div.xpath('@alt').extract_first()
        yield scrapy.Request(url=img,meta={'title':title} ,callback=self.download_c)

    def download_c(self,response):
        dirpath = r'C:\Users\dengc\Desktop\MZT_陆梓琪'
        if not os.path.exists(dirpath):
            os.mkdir(dirpath)
        num1 = random.randint(1,10000)
        num2 = random.randint(1,10000)
        num3 = num1 + num2
        img_path = os.path.join(dirpath,response.meta['title']) + str(num3) +  '.jpg'

        # 保存
        with open(img_path, 'wb')as fp:
            fp.write(response.body)
        print('{}--保存完成'.format(img_path))


