# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#
# class ProExamplePipeline(object):
#     def process_item(self, item, spider):
#         return item

import os,time,csv, json,sqlite3, pymongo, pymysql
import logging
from openpyxl import Workbook
from xml.dom.minidom import Document
from scrapy.pipelines.files import FilesPipeline
from .dict2sql import dict2sql_insert

from scrapy.conf import settings
from .items import LuhanItem

# print(dict(settings),settings["BOT_NAME"])  #获取settings配置


class TagPipeline(object):
    def process_item(self, item, spider):
        item['check_time'] = time.strftime('%y%m%d', time.localtime())
        item['spider_name'] = spider.name
        return item

class CsvPipeline(object):

    # def __init__(self, CSVNAME):
    #     self.filename = CSVNAME

    def open_spider(self, spider):
        obj_item = LuhanItem()
        self.f = open(spider.name+".csv", "w",newline="", encoding="utf-8")
        self.csv = csv.DictWriter(self.f, fieldnames=list(obj_item.fields.keys()))
        if not self.f.tell():

            self.csv.writeheader()

    def process_item(self, item, spider):
        self.csv.writerow(dict(item))
        return item

    def close_spider(self, spider):
        self.f.close()
    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         CSVNAME=crawler.settings.get("CSVNAME")
    #     )

class Csv_Pipeline(object):

    def open_spider(self, spider):
        self.f = open(spider.name+".csv", "w",newline="", encoding="utf-8")
        self.csv = csv.DictWriter(self.f, fieldnames=LuhanItem.save_filed)
        if not self.f.tell():
            self.csv.writeheader()
        self.ft = open(spider.name+".txt","w",encoding="utf-8")

    def process_item(self, item, spider):
        data = dict(item)
        a = LuhanItem.save_filed
        data = dict([(i,v) for i,v in data.items() if i in a])

        self.csv.writerow(data)
        self.ft.write(item.get("fans_com")+"\n")

        return item

    def close_spider(self, spider):
        self.f.close()
        self.ft.close()

class JsonPipeline(object):
    # def __init__(self, JSONNAME):
    #     self.jsonname = JSONNAME

    def open_spider(self, spider):
        self.f = open(spider.name+".json", "w", encoding="utf-8")

    def process_item(self, item, spider):
        json.dump(dict(item), self.f, ensure_ascii=False)
        return item

    def close_spider(self, spider):
        self.f.close()

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         JSONNAME=crawler.settings.get("JSONNAME")
    #     )


class ExcelPipeline(object):
    def open_spider(self, spider):
        self.wb = Workbook(write_only=True)
        self.ws = self.wb.create_sheet(title=spider.name)
        self.KeysWritten = False

    def process_item(self, item, spider):
        # write keys
        if not self.KeysWritten:
            self.ws.append(list(map(str, dict(item).keys())))
            self.KeysWritten = True

        # write values
        self.ws.append(list(map(str, dict(item).values())))
        return item

    def close_spider(self, spider):
        self.wb.save(spider.name + '.xls')


class TxtPipeline(object):
    def open_spider(self, spider):
        self.f = open(spider.name + '.txt', 'w', encoding='utf-8')
        self.KeysWritten = False

    def process_item(self, item, spider):
        # write keys
        if not self.KeysWritten:
            self.f.write('\t'.join(map(str, dict(item).keys())) + '\n')
            self.KeysWritten = True

        # write values
        self.f.write('\t'.join(map(str, dict(item).values())) + '\n')
        return item

    def close_spider(self, spider):
        self.f.close()


class XmlPipeline(object):
    def open_spider(self, spider):
        self.doc = Document()
        self.node_items = self.doc.createElement('items')

    def process_item(self, item, spider):
        self.var2xmlnode(k='item', v=dict(item), p=self.node_items, r=self.doc)
        return item

    def close_spider(self, spider):
        self.doc.appendChild(self.node_items)
        with open(spider.name + '.xml', 'w', encoding='utf-8') as f:
            f.write(self.doc.toprettyxml())

    def var2xmlnode(self, k, v, p, r):
        '''
        python var to xml node
        :param k: var name(type: str)
        :param v: var value(type: all types)
        :param p: parents node(type: xml node)
        :param r: root Document
        :return: None
        '''
        node_k = r.createElement(k)

        # dict
        if isinstance(v, dict):
            for ik, iv in v.items():
                self.var2xmlnode(k=ik, v=iv, p=node_k, r=r)

        # list, tuple
        elif isinstance(v, (list, tuple)):
            for i in v:
                self.var2xmlnode(k='value', v=i, p=node_k, r=r)

        # str, num
        else:
            node_v = r.createTextNode(str(v))
            node_k.appendChild(node_v)

        p.appendChild(node_k)



class SqlitePipeline(object):
    def open_spider(self, spider):
        try:
            self.connect = sqlite3.connect(spider.name + '.db')
        except Exception as e:
            logging.log(logging.ERROR, 'PipelineSqlite open_spider: ' + str(e))
        else:
            self.cursor = self.connect.cursor()
            self.TableCreated = False

    def process_item(self, item, spider):
        try:
            # create table
            if not self.TableCreated:
                self.cursor.execute(self.sqlcreatetable(t_=spider.name, **dict(item)))
                self.TableCreated = True

            # insert
            self.cursor.execute(dict2sql_insert(t_=spider.name, **dict(item)))
        except Exception as e:
            logging.log(logging.ERROR, 'PipelineSqlite process_item: ' + str(e))
        else:
            self.connect.commit()
        return item

    def close_spider(self, spider):
        try:
            self.cursor.close()
            self.connect.close()
        except Exception as e:
            logging.log(logging.ERROR, 'PipelineSqlite close_spider: ' + str(e))

    def sqlcreatetable(self, t_, **kwargs):
        '''
        dict to sql sentence(create table)
        num type will save as real
        other types will save as text

        :param t_: table name(type: str)
        :param kwargs: dict
        :return: sql sentence of create table(type: str)
        '''
        create_table = 'CREATE TABLE IF NOT EXISTS ' + str(t_)

        required_columns = 'id int primary key, isDelete bit default 0, '

        i_ = lambda i: str(i[0]) + (' real' if isinstance(i[-1], (int, float)) else ' text')
        optional_columns = ', '.join(map(i_, kwargs.items()))

        return create_table + '(' + required_columns + optional_columns + ')'



class MongoPipeline(object):
    def __init__(self, MONGOHOST, MONGOPORT, MONGODB, MONGOTABLE):
        self.mongohost = MONGOHOST
        self.mongoport = MONGOPORT
        self.mongodb = MONGODB
        self.mongotable = MONGOTABLE

    def open_spider(self, spider):
        try:
            self.mongo = pymongo.MongoClient(self.mongohost, self.mongoport)
            self.db = self.mongo[self.mongodb]
        except Exception as e:
            logging.log(logging.ERROR,'PipelineMongodb open_spider: ' + str(e))
    def process_item(self, item, spider):
        try:
            self.db[self.mongotable].insert(dict(item))
        except Exception as e:
            logging.log(logging.ERROR, 'PipelineMongodb open_spider: ' + str(e))
        return item

    def close_spider(self, spider):
        self.mongo.close()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            MONGOHOST=crawler.settings.get("MONGOHOST"),
            MONGOPORT=crawler.settings.get("MONGOPORT"),
            MONGODB=crawler.settings.get("MONGODB"),
            MONGOTABLE=crawler.settings.get("MONGOTABLE"),
        )


class MysqlPipeline(object):
    def __init__(self,HOST,PORT,USER,PWD,DB):
        self.host = HOST
        self.port = PORT
        self.user = USER
        self.pwd = PWD
        self.db = DB

    def open_spider(self,spider):
        self.con = pymysql.connect(
            hsot = self.host,
            port = self.port,
            user = self.user,
            passwd = self.pwd,
            db = self.db,
            charset = "utf-8",
        )
        self.cur = self.con.cursor()

    def process_item(self,item,spider):
        print(type(item),item)
        sql = "insert into %s values (none,%s,%s)" %(self.db,item['title'],item['img_url'])
        print(sql)
        try:
            self.cur.execute(sql)
            self.con.commit()
        except Exception as e:
            self.con.rollback()
        return item

    def close_spider(self,spider):
        self.con.close()

    # 这种语句创建出来的表，很不负责，建议自己创建表
    def sqlcreatetable(self, t_, v_=255, **kwargs):
        '''
        dict to sql sentence(create table)
        num type will save as float
        other types will save as varchar(v_)

        :param t_: table name(type: str)
        :param v_: length of varchar(type: int)
        :param kwargs: dict
        :return: sql sentence of create table(type: str)
        '''
        create_table = 'CREATE TABLE IF NOT EXISTS ' + str(t_)

        required_columns = 'id int auto_increment primary key not null, isDelete bit default 0, '

        i_ = lambda i: str(i[0]) + (' float' if isinstance(i[-1], (int, float)) else ' varchar(%d)' % v_)
        optional_columns = ', '.join(map(i_, kwargs.items()))

        return create_table + '(' + required_columns + optional_columns + ')'


    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            HOST = crawler.settings.get("HOST"),
            PORT = crawler.settings.get("PORT"),
            USER = crawler.settings.get("USER"),
            PWD = crawler.settings.get("PWD"),
            DB = crawler.settings.get("DB"),
        )