# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Spider02Spider(CrawlSpider):
    name = 'spider02'
    allowed_domains = ['meituba.com']
    start_urls = ['http://meituba.com/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    # class LxmlLinkExtractor(FilteringLinkExtractor):
    #     def __init__(self, allow=(), deny=(), allow_domains=(), deny_domains=(), restrict_xpaths=(),
    #                  tags=('a', 'area'), attrs=('href',), canonicalize=False,
    #                  unique=True, process_value=None, deny_extensions=None, restrict_css=(),
    #                  strip=True):
    #
    # #    allow   接收正则表达式 ，用于提取需要获取的url,
    # #    deny    接收正则表达式 ，用于过滤不需要获取的url,
    # #    allow_domains 域名： 需要抓取的域名
    # #     deny_domains   域名： 不需要抓取的
    # #     restrict_xpaths   接收一个xpath 语法，配合allow 使用，先过滤掉部分标签
    #
    # Rule
    # 参数说明：
    #
    # # follow  是否跟进抓取，也就获取到第一个页面源码之后是否抓取这个页面的url，默认为true 跟进抓取，设置为flase 不跟进抓取
    #
    # # callback 回调函数，特别注意：不能使用parse这个解析函数
    #
    # # process_links  当匹配到url之后，调用process_links 的方法发送请求

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
