# -*- coding: utf-8 -*-

# Scrapy settings for jd_goods project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'jd_goods'

SPIDER_MODULES = ['jd_goods.spiders']
NEWSPIDER_MODULE = 'jd_goods.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'jd_goods (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

COOKIES_ENABLED = False

RETRY_ENABLED = True
RETRY_HTTP_CODES = [301, 302, 500, 502, 503, 504, 400, 403, 404, 408]
RETRY_TIMES = 5

#LOG_FILE = '/Users/QiyaoWei/Desktop/f.txt'

"""
FEED_URI = "/Users/QiyaoWei/Desktop/demo.csv"
FEED_FORMAT = 'csv'
FEED_EXPORT_ENCODING = 'gbk'
"""

"""
FEED_EXPORTERS = {'csv': 'jd_goods.spiders.csv_exporter.JdGoodsCsvExporter'}
FIELDS_TO_EXPORT = [
	'item_first_cat',
	'item_second_cat',
	'item_third_cat',
	'item_name',
	'item_id',
	'item_price',
	'item_num_comments',
	'item_discounts']
"""

DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'referer': 'https://www.jd.com/',
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"
}

"""
MY_USER_AGENT = [
    #"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",]
    #"Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",]
    #"Mozilla/5.0(iPod;U;CPUiPhoneOS4_3_3likeMacOSX;en-us)AppleWebKit/533.17.9(KHTML,likeGecko)Version/5.0.2Mobile/8J2Safari/6533.18.5",]
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Mobile/14G60 MicroMessenger/6.5.18 NetType/WIFI Language/en"]
    #"Mozilla/5.0 (Linux; Android 5.1.1; vivo Xplay5A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 T7/9.3 baiduboxapp/9.3.0.10 (Baidu; P1 5.1.1)"]
    #"Mozilla/5.0 (iPhone 92; CPU iPhone OS 10_3_2 like Mac OS X) AppleWebKit/603.2.4 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.7.2 Mobile/14F89 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1"]
"""

SPIDER_MIDDLEWARES = {
    'jd_goods.middlewares.JdGoodsSpiderMiddleware': 543,
}

DOWNLOADER_MIDDLEWARES = {
    'jd_goods.middlewares.JdGoodsDownloaderMiddleware': 543,
    #'jd_goods.middlewares.MyHttpProxyMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

ITEM_PIPELINES = {
    #'jd_goods.pipelines.JdGoodsPipeline': 300,
    'jd_goods.pipelines.MasterPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'




#Redis
# 启用Redis调度存储请求队列
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 确保所有的爬虫通过Redis去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'

# 默认请求序列化使用的是pickle 但是我们可以更改为其他类似的。PS：这玩意儿2.X的可以用。3.X的不能用
# SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"
#SCHEDULER_QUEUE_KEY = '%(spider)s:requests'

# 不清除Redis队列、这样可以暂停/恢复 爬取
SCHEDULER_PERSIST = True
SCHEDULER_FLUSH_ON_START = True

# 使用优先级调度请求队列 （默认使用）
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# 可选用的其它队列
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

# 最大空闲时间防止分布式爬虫因为等待而关闭
# 这只有当上面设置的队列类是SpiderQueue或SpiderStack时才有效
# 并且当您的蜘蛛首次启动时，也可能会阻止同一时间启动（由于队列为空）
#SCHEDULER_IDLE_BEFORE_CLOSE = 20

# 序列化项目管道作为redis Key存储
#REDIS_ITEMS_KEY = '%(spider)s:items'

# 默认使用ScrapyJSONEncoder进行项目序列化
# You can use any importable path to a callable object.
#REDIS_ITEMS_SERIALIZER = 'json.dumps'

# 指定连接到redis时使用的端口和地址（可选）
#REDIS_HOST = 'localhost'
#REDIS_PORT = 6379

# 指定用于连接redis的URL（可选）
# 如果设置此项，则此项优先级高于设置的REDIS_HOST 和 REDIS_PORT
REDIS_URL = 'redis://user:test@localhost:6379'

# 自定义的redis参数（连接超时之类的）
# REDIS_PARAMS  = {}

# 自定义redis客户端类
# REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient'

# 如果为True，则使用redis的'spop'进行操作。
# 如果需要避免起始网址列表出现重复，这个选项非常有用。开启此选项urls必须通过sadd添加，否则会出现类型错误。
REDIS_START_URLS_AS_SET = True

# RedisSpider和RedisCrawlSpider默认 start_urls 键
REDIS_START_URLS_KEY = '%(name)s:start_urls'

# 设置redis使用utf-8之外的编码
# REDIS_ENCODING = 'latin1'