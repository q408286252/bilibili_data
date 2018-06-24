#!/usr/bin/env python
# coding=utf-8

import scrapy
from crawl_data.items import Crawl_bilibili

class VmoiveSpider(scrapy.Spider):
    # name是spider最重要的属性, 它必须被定义。同时它也必须保持唯一
    name = 'vmoive'
    # 可选定义。包含了spider允许爬取的域名(domain)列表(list)
    allowed_domains = ['space.bilibili.com']
    #Url 列表
    start_urls = [
        'https://space.bilibili.com/1/#/'
    ]

    def parse(self, response):
        #日志
        self.log('item page url is ==== ' + response.url)
        #姓名
        # item['name'] = response.xpath("//span[@id='h-name']/text()")[0].extract()
        #moivelist = response.xpath('//div[@class="n-inner clearfix"]')
        moivelist = response.xpath('//*[@id="navigator"]/div/div[1]')
        print('您好这是文件' , moivelist)
        for m in moivelist:
            item = Crawl_bilibili()
            #视频数
            item['Video amount'] = m.xpath('./div[@class="n-tab-links"]/a[@class="n-btn n-video n-audio n-article n-album"]/span[@class="n-num"]/text()')[0].extract()
            #播放量
            item['Play amount'] = m.xpath('./div[@class="n-statistics"]/div/p[@class="n-data n-bf"]/text()')[0].extract()
            #粉丝数
            item['fans'] = m.xpath('./div[@class="n-statistics"]/a[@class="n-data n-fs"]/@title')[0].extract()
            #母猪指数: 算一下每个视频的更新周期 排除异常值然后算平均每期时间  算方差算出每只母猪出产的稳定率
        #保存所有粉丝数超过50w的人id
        print(item)
        '''
        with open("F:/data/crawl_data/text.txt","w+",encoding="utf-8") as p:
            p.write(pass)
         '''   
        yield item
 
