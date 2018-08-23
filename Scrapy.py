#rdb --command json /Users/QiyaoWei/Documents/CardinalOp/jd_goods/dump.rdb > memory.json

import scrapy
import sys
import time
sys.path.append("..")
from jd_goods.items import JdRedisItem
from jd_goods.items import JdGoodsItem
#from jd_goods.items import JdGoodsLoader
#from scrapy_redis.spiders import RedisSpider
from redis import Redis
import json

class Scrapy(scrapy.Spider):

    name = "jd_goods"
    allowed_domains = ["jd.com"]
    #redis_key = 'jd_goods:start_urls'
    start_urls = ["https://www.jd.com/allSort.aspx"]

    def parse(self, response):

        categories = response.xpath('//div[@class="category-item m"]')
        for cat in categories[1:2]:
            first_cat = cat.xpath('.//h2[@class="item-title"]/span/text()').extract()[0]
            subcategories = cat.xpath('.//dl[@class="clearfix"]')
            for sub in subcategories:
                second_cat = sub.xpath('.//dt/a/text()').extract()[0]
                subsubcategories = sub.xpath('.//dd/a')
                for subsub in subsubcategories:
                    third_cat = subsub.xpath('.//text()').extract()[0]
                    url = subsub.xpath('.//@href').extract()[0]
                    url = "https:" + url
                    redis_item = JdRedisItem()
                    redis_item['url'] = url
                    yield redis_item
                    goods_item = JdGoodsItem()
                    goods_item['item_first_cat'] = first_cat
                    goods_item['item_second_cat'] = second_cat
                    goods_item['item_third_cat'] = third_cat
                    goods_item['item_url'] = url
                    yield goods_item


        r = Redis()
        while True:
            a = r.lpop('JD:items')
            if a is None:
                time.sleep(10)
            else:
                a = json.load(a)
                if len(a.keys()) == 1 and 'test' in a.keys():
                    r.lpush('item', a) #d['test'][0]
                elif len(a.keys()) == 1 and 'urls' in a.keys():  # xxxxxxxxxxxxxxxxxx
                    yield scrapy.Request(a['urls'][0], callback = self.scrape, dont_filter = True)
                else:
                    print("oops")


    def scrape(self, response):
            #检验是否标准格式，如不是则刷新
            r = response.xpath("//li[@class='gl-item']")

            if len(r) == 0: #刷新
                time.sleep(3)
                yield scrapy.Request(response.url, callback = self.p, dont_filter = True)
            else:
                redis_item = JdRedisItem()
                redis_item['url'] = response.url
                yield redis_item
                """
                #爬+翻页xxxxxxxxxxxxxxxxxxxxxxxxxx
                for i in r:
                    sku = i.xpath("div/@data-sku").extract()[0]
                    name = i.xpath("div/div[starts-with(@class, 'p-name')]/a/em/text()").strip()
                p = response.xpath("//div[@class='page clearfix']/div/span[1]/a[last()]")
                if p.xpath("text()") != '下一页':
                    print(response.url + "   done?")
                else:
                    yield scrapy.Request("https://list.jd.com/" + p.xpath("@href").extract()[0], callback = self.parse, dont_filter = True)
                """

    def p(self, response):
            #再次检验标准格式，其他格式，以及空白页
            if len(response.xpath("//li[@class='gl-item']")) == 0:

                r = response.xpath("//div[@class='item-inner']") #其他格式
                if len(r) == 0:
                    print("Nothing on %s!", response.url)
                else:
                    for i in r:
                        #从大类进去，大类不行再小类
                        yield scrapy.Request("https://" + i.xpath("h3/a/@href").extract()[0], callback = self.other, dont_filter = True)
            else:
                #标准
                redis_item = JdRedisItem()
                redis_item['url'] = response.url
                yield redis_item

    def other(self, response):
            #爬取其他格式???，并预防特殊情况
            a = response.xpath("//li[@class='gl-item']")
            #b = response.xpath("//div[@class='p-btn']") #ul "clearfix" is not available

            if len(a) != 0:
                #标准
                redis_item = JdRedisItem()
                redis_item['url'] = response.url
                yield redis_item

#            elif len(b) != 0:
#                #其他格式，应该只有一种
#                #翻页方法类似
#                #for i in b:
#                #   id = i.xpath("a[last()]/@data-id")
#                #   name = ...
#                print("wtf!")
#                pass

            else:
                r = response.xpath("//div[@class='item-inner']")
                if len(r) == 0:
                    print("Something weird happening on %s!", response.url)
                else:
                    #从小类进
                    for i in r:
                        a = i.xpath("div[@class='ext']")
                        for ia in a:
                            yield scrapy.Request("https://" + ia.xpath("a/@href").extract()[0], callback = self.other, dont_filter = True)