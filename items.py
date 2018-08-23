# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
#from scrapy.loader import ItemLoader
#from scrapy.loader.processors import MapCompose, TakeFirst, Join

class JdRedisItem(scrapy.Item):
    url = scrapy.Field()
    """
    item_first_cat    = scrapy.Field()
    item_second_cat   = scrapy.Field()
    item_third_cat    = scrapy.Field()
    item_name         = scrapy.Field()
    item_id           = scrapy.Field()
    item_price        = scrapy.Field()
    item_num_comments = scrapy.Field()
    item_discounts    = scrapy.Field()
    """

class JdGoodsItem(scrapy.Item):
    item_first_cat = scrapy.Field()
    item_second_cat = scrapy.Field()
    item_third_cat = scrapy.Field()
    item_url = scrapy.Field()

"""
class JdGoodsLoader(ItemLoader):
    default_item_class = JdGoodsItem
    default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    description_out = Join()
"""