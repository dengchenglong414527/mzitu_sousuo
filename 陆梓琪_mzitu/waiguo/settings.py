# -*- coding: utf-8 -*-

# Scrapy settings for waiguo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'waiguo'

SPIDER_MODULES = ['waiguo.spiders']
NEWSPIDER_MODULE = 'waiguo.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#   'cookie': '__cfduid=dfaca3481653f15bbc57474ecee70ec331542797723; cid=rBsWH1v1OZsoiwAjE/gkAg==; _pxvid=f3a6b7f0-ed7b-11e8-8849-b756df2c9e8c; _ga=GA1.2.1712065898.1542797734; _gid=GA1.2.735578177.1542797734; _hp2_ses_props.973801186=%7B%22ts%22%3A1542797735614%2C%22d%22%3A%22www.crunchbase.com%22%2C%22h%22%3A%22%2F%22%7D; wcsid=NZr7oRZKpaJE8wQM3F6pZ0H6jrAJ23B6; hblid=2Gd8mUNOh5H45gpx3F6pZ0HbA2J6rr8j; _okdetect=%7B%22token%22%3A%2215427977427600%22%2C%22proto%22%3A%22https%3A%22%2C%22host%22%3A%22www.crunchbase.com%22%7D; olfsk=olfsk8382648814101858; _okbk=cd4%3Dtrue%2Cvi5%3D0%2Cvi4%3D1542797744781%2Cvi3%3Dactive%2Cvi2%3Dfalse%2Cvi1%3Dfalse%2Ccd8%3Dchat%2Ccd6%3D0%2Ccd5%3Daway%2Ccd3%3Dfalse%2Ccd2%3D0%2Ccd1%3D0%2C; _ok=1554-355-10-6773; __qca=P0-1749646553-1542797750264; _pendo_visitorId.c2d5ec20-6f43-454d-5214-f0bb69852048=_PENDO_T_mTU5vFNkrZW; _pendo_meta.c2d5ec20-6f43-454d-5214-f0bb69852048=2816097502; _hp2_props.973801186=%7B%22Logged%20In%22%3Afalse%2C%22Pro%22%3Afalse%2C%22cbPro%22%3Afalse%2C%22apptopia-lite%22%3Afalse%2C%22apptopia-premium%22%3Afalse%2C%22builtwith%22%3Afalse%2C%22ipqwery%22%3Afalse%2C%22siftery%22%3Afalse%2C%22similarweb%22%3Afalse%2C%22bombora%22%3Afalse%2C%22owler%22%3Afalse%7D; _hp2_id.973801186=%7B%22userId%22%3A%224503740049580252%22%2C%22pageviewId%22%3A%227671508462114607%22%2C%22sessionId%22%3A%228540688450066446%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _px3=7765c7fb7f504e3c1e010f93e922f5f554ff01e6c5f34bbdbcf77d8ea43c6902:1uWNKydkaJcByaR3008yHJvlQ12yLpbcgH6pAVfGk1kWe/HdoqbFbOqfFazLYgFX8Voa98mgPTklX0XdxDyNwA==:1000:T2VOcoiqX0C25Rcwa4c5dkV7J69j3eLaFvNd9O6/wB4c/Fro9QirJKfS/68Gwq5XbJtSFI6BOxPBFPGQSGaGiquLJoV2DcnZRwpScskLyIEnkCfFuFvv8uiI9GtT011c59afG4RlkuM9b3veCYahOuytf13L7Rq+9WGDpp7o05g=; _oklv=1542801999840%2CNZr7oRZKpaJE8wQM3F6pZ0H6jrAJ23B6',
#   # 'referer': 'https://www.crunchbase.com/',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'waiguo.middlewares.WaiguoSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'waiguo.middlewares.WaiguoDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'waiguo.pipelines.WaiguoPipeline': 300,
# }

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
LOG_LEVEL = 'ERROR'