# -*- coding: utf-8 -*-

# Scrapy settings for pro_example project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'pro_example'

SPIDER_MODULES = ['pro_example.spiders']
NEWSPIDER_MODULE = 'pro_example.spiders'


LOG_LEVEL = "DEBUG"
# LOG_LEVEL = "INFO"
# LOG_LEVEL = "WARNING"
# LOG_LEVEL = "ERROR"
# LOG_LEVEL = "CRITICAL"
# LOG_FILE = './log.log'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'pro_example (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'pro_example.middlewares.ProExampleSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'pro_example.middlewares.ProExampleDownloaderMiddleware': 543,
    BOT_NAME + '.middlewares.RandomHeaders': 100,
    # BOT_NAME + '.middlewares.RandomIP': 200,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
   # 'scrapy.extensions.telnet.TelnetConsole': None,
   #  BOT_NAME + '.extensions.EndMail': 100,    #发送邮件，已测OK
}


# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'pro_example.pipelines.ProExamplePipeline': 300,
#}


DOWNLOAD_DELAY = 0

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 0.2
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 6
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'




ITEM_PIPELINES = {
    
    # BOT_NAME + '.pipelines.TagPipeline': 100,
    BOT_NAME + '.pipelines.Csv_Pipeline': 200,
    BOT_NAME + '.pipelines.JsonPipeline': 300,
    # BOT_NAME + '.pipelines.ExcelPipeline': 400,
    # BOT_NAME + '.pipelines.TxtPipeline': 500,
    # BOT_NAME + '.pipelines.XmlPipeline': 600,
    # BOT_NAME + '.pipelines.SqlitePipeline': 700,
    # BOT_NAME + '.pipelines.MongoPipeline': 800,
    # BOT_NAME + '.pipelines.MysqlPipeline': 900,
}





# mongodb
MONGODB_CONFIG = {
    'host': '10.0.15.80',
    'port': 27017
}

# mysql
MYSQL_CONFIG = {
    'host': '10.0.15.80',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'scrapy_db',
    'charset': 'utf8mb4',
}





#########
#send_mail
#########
MAIL_HOST = 'smtp.163.com'
MAIL_PORT = 25
MAIL_USER = 'l475378094@163.com'
MAIL_PASS = '00000000'
MAIL_FROM = 'l475378094@163.com'
MAIL_TO = '475378094@qq.com'
#########
#send_mail
#########
