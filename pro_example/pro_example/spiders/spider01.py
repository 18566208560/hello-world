# -*- coding: utf-8 -*-
import scrapy
from pro_example.items import Spider01Item


class Spider01Spider(scrapy.Spider):
    name = 'spider01'
    # allowed_domains = ['meituba.com']
    start_urls = ['http://www.meituba.com/']

    def parse(self, response):
        # print(response.request.headers)
        print(response.url)

        yield scrapy.Request(url="http://www.baidu.com/",callback=self.parse_info,cookies={"BAIDUID":"1000","H_WISE_SIDS":"100000","a":"b"})

    def parse_info(self,response):
        print("0000000000000000",response.url)
        print(response.request.headers)




 # url=要请求的url,
    #callback =回调函数，
    #headers = 请求头，
    #ookies= 接收字典 {"sd":"sdf"}
    #meta= 给回调函数传参数，字典类型，通过解析函数  response.meta.get("id")
    #dont_filter 去重

#https://m.weibo.cn/api/container/getIndex?uid=1537790411&luicode=10000011&lfid=100103type%3D1%26q%3D%E9%B9%BF%E6%99%97&featurecode=20000320&type=uid&value=1537790411&containerid=1076031537790411&since_id=4267937844374459
#https://m.weibo.cn/api/container/getIndex?uid=1537790411&luicode=10000011&lfid=100103type%3D1%26q%3D%E9%B9%BF%E6%99%97&featurecode=20000320&type=uid&value=1537790411&containerid=1076031537790411&since_id=4267937844374459

#https://m.weibo.cn/api/container/getIndex?uid=1537790411&luicode=10000011&lfid=100103type%3D1%26q%3D%E9%B9%BF%E6%99%97&featurecode=20000320&type=uid&value=1537790411&containerid=1076031537790411&since_id=4259800978425832
#https://m.weibo.cn/api/container/getIndex?uid=1537790411&luicode=10000011&lfid=100103type%3D1%26q%3D%E9%B9%BF%E6%99%97&featurecode=20000320&type=uid&value=1537790411&containerid=1076031537790411&since_id=4259800978425832

4249766458657049
4249766458657049

