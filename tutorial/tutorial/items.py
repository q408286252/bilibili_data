# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyDemoItem(scrapy.Item):

    #  排名
    ranking = scrapy.Field()
    # 动画名称
    movie_name = scrapy.Field()
    # 集数 年份 导演 原作者 角色设定
    data_text = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 评论人数
    score_num = scrapy.Field()

