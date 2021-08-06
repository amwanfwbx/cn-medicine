# -*- coding: utf-8 -*-

# Scrapy settings for eatspiders project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'eatspiders'

SPIDER_MODULES = ['eatspiders.spiders']
NEWSPIDER_MODULE = 'eatspiders.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'eatspiders (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'zh-cn',
  'cookie': 'cna=36lwFIo3XSUCAT2BsXY0bj0F; enc=oWQ%2FcPe7uGBik70Te5ss9EEmNxd3eR4fOO4Nxi%2Bpqz8QFUZYrCYbWNoBrlM1DPEbiL%2BdUoCzTzij%2BEIRkHnQHA%3D%3D; lid=reebok%E5%AE%98%E6%96%B9%E6%97%97%E8%88%B0%E5%BA%97%3A%E7%9B%9B%E9%94%8B; hng=CN%7Czh-CN%7CCNY%7C156; t=dc5913274f17ecfce36e95f7688b25a2; _tb_token_=e0504135e3767; cookie2=1e2f40602629fad1b4481e84702463aa; _m_h5_tk=57f10c6fb3b3379b91115cba9406b663_1607587064491; _m_h5_tk_enc=4e3600ac0a864fe6148a79f12888fe2b; cq=ccp%3D1; _bl_uid=Rbk24iCbikyf87d0n36Rjw3dsC53; pnm_cku822=; xlly_s=1; OZ_SI_2061=sTime=1607579572&sIndex=44; OZ_1U_2061=vid=vfd1b7b5195c33.0&ctime=1607655169&ltime=1607654820; OZ_1Y_2061=erefer=-&eurl=https%3A//uniqlo.tmall.com/&etime=1607580082&ctime=1607655169&ltime=1607654820&compid=2061; tfstk=catlBOmm5U754Z7D50sWInNq-guAwjHP_BRv0nTtRCIKYDfD8rzZP83caQxLR; l=eBMowAxlvaQfEePaBOfwourza77OSIRAguPzaNbMiOCP_S1p5A9RWZJqO6L9C3GNhsQJR3uKcXmQBeYBqncXvK9UNoVoKvDmn; isg=BFxc6loMb73taB_Ci8u0TuzgLXoO1QD_w2T4yTZdaMcqgfwLXuXQj9I34eF5CThX'

}
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'zh,zh-CN;q=0.9,zh-HK;q=0.8',
# }
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'eatspiders.middlewares.EatspidersSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'eatspiders.middlewares.EatspidersDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'eatspiders.pipelines.EatspidersPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
