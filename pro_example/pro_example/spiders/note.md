####创建项目

```python
scrapy startproject pro_example
```

####创建爬虫

```
scrapy genspider spider01 meituba.com
```

####创建通用爬虫

```
scrapy genspider -t crawl spider02 meituba.com
```

####执行爬虫

```
scrapy crawl mt     # mt是爬虫名称
```

####简单数据存储

```
scrapy crawl mt   -o "meitu.csv"   # json  jsonlines
```



