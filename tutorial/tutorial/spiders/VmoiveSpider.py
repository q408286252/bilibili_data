#!/usr/bin/env python
# coding=utf-8

import scrapy
from tutorial.items import ScrapyDemoItem

class VmoiveSpider(scrapy.Spider):
    # name是spider最重要的属性, 它必须被定义。同时它也必须保持唯一
    name = 'vmoive'

    # 可选定义。包含了spider允许爬取的域名(domain)列表(list)
    allowed_domains = ['bangumi.tv']
    #Url 列表 42 页到1020
    #start_urls = ['http://bangumi.tv/anime/browser?sort=rank&page=1']
    start_urls = ['http://bangumi.tv/anime/browser?sort=rank&page='+ str(i) for i in range(1,43)]
    def parse(self, response):
        #日志
        self.log('item page url is ==== ' + response.url)

        #目标内容 有很多
        moivelist = response.xpath('//li[@class="item odd clearit" or @class="item even clearit"]')
        for m in moivelist:
            item = ScrapyDemoItem()
            item['ranking'] = m.xpath('./div/span/text()')[0].extract()
            item['movie_name'] = m.xpath('./div/h3/a/text()')[0].extract()
            item['data_text'] = m.xpath('./div/p[@class="info tip"]/text()')[0].extract()
            item['score'] = m.xpath('./div/p[@class="rateInfo"]/small/text()')[0].extract()
            item['score_num'] = m.xpath('./div/p[@class="rateInfo"]/span/text()')[0].extract()
            with open("F:/data/data.txt","a+",encoding='UTF-8') as p:
                p.write(item['ranking'])
                p.write('\t'+ item['movie_name'])
                p.write('\t'+ item['data_text'].lstrip("\n").strip())
                p.write('\t'+ item['score'])
                p.write('\t'+ item['score_num']+"\n")
            yield item