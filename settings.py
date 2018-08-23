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
# Default Redis Scheduler
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Default Redis duplicate filter
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'

#SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"
#SCHEDULER_QUEUE_KEY = '%(spider)s:requests'

# Does the scheduler clear after a pause?
SCHEDULER_PERSIST = True
SCHEDULER_FLUSH_ON_START = True

# Default Redis queue
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# Other queues
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

# You can use any importable path to a callable object.
#REDIS_ITEMS_SERIALIZER = 'json.dumps'

#REDIS_HOST = 'localhost'
#REDIS_PORT = 6379

# Overrides REDIS_HOST and REDIS_PORT if set
REDIS_URL = 'redis://user:test@localhost:6379'

# Must use sadd and spop if set, instead of lpush and lpop
REDIS_START_URLS_AS_SET = True

# Default start url key
REDIS_START_URLS_KEY = '%(name)s:start_urls'
