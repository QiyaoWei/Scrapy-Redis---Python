# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
from jd_goods.items import JdRedisItem
from jd_goods.items import JdGoodsItem

class MasterPipeline(object):
    def __init__(self):
        self.redis_url = 'redis://user:test@localhost:6379'
        self.r = redis.Redis.from_url(self.redis_url, decode_responses = True)

    def process_item(self, item, spider):
        if isinstance(item, JdRedisItem):
            self.r.lpush('jdspider:start_urls', item['url'])
        elif isinstance(item, JdGoodsItem):
            self.r.lpush('item', item)
        else:
            print("Not an item!")

"""
from scrapy.exceptions import DropItem
class JdGoodsPipeline(object):

    def __init__(self):
        self.seen = set()

    def process_item(self, item, spider):
        if 'item_id' in item.keys():
            if item['item_id'] in self.seen:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.seen.add(item['item_id'])
                return item
"""

"""
class RedisPipeline(object):
    def process_item(self, item, spider):
        key = self.item_key(item, spider)
        data = self.serialize(item)
        self.server.rpush(key, data)
        return item

    def item_key(self, item, spider):
        
        :param item: Given item
        :param spider: Given spider
        :return: Redis key
        
        return self.key % {'spider': spider.name}
"""