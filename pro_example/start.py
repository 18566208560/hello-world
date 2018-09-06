import os
from scrapy import cmdline

# from scrapy.conf import settings
#
# print(dict(settings),settings["BOT_NAME"])  #获取settings配置


b = ["luhan","spider01"]
print(b)
a = int(input("请输入爬虫名："))-1
os.system("scrapy crawl "+b[a])  #



# cmdline.execute("scrapy crawl spider01".split()) #scrapy启动项目方法


# a = list("abcdefg")
#
# for i in a:
#     print(i,i)
