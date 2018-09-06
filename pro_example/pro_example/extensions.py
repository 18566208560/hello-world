# -*- coding: utf-8 -*-

import logging
import smtplib
from email.mime.text import MIMEText
from scrapy import signals
from scrapy.conf import settings
from scrapy.utils.engine import get_engine_status


def send_mail(subject='subject', content='content'):
    # mail server
    mail_host = settings['MAIL_HOST']
    mail_port = settings['MAIL_PORT']
    mail_user = settings['MAIL_USER']
    mail_pwd = settings['MAIL_PASS']

    # mail message
    message = MIMEText(content, 'plain', 'utf-8')
    message['Subject'] = subject
    message['From'] = settings['MAIL_FROM']
    message['To'] = settings['MAIL_TO']

    # send mail
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, mail_port)
        smtpObj.login(mail_user, mail_pwd)
        smtpObj.sendmail(message['From'], message['To'], message.as_string())
        smtpObj.quit()
    except smtplib.SMTPException as e:
        logging.log(logging.ERROR, 'send_mail: ' + str(e))


# EndMail: perfect
class EndMail(object):
    @classmethod
    def from_crawler(cls, crawler):
        o = cls(crawler)
        # (方法，信号)
        crawler.signals.connect(o.spider_closed, signal=signals.spider_closed)

        return o

    def __init__(self, crawler):
        self.crawler = crawler

    def spider_closed(self, spider):
        subject = 'Scrapy Server: Spider %s closed, please check out on your server.' % spider.name
        content = 'Spider name: %s' % spider.name

        content += '\n' + '-' * 20 + '\n'
        content += 'Spider stats:\n'
        content += '\n'.join('%s: %s' % i for i in self.crawler.stats.get_stats().items())

        content += '\n' + '-' * 20 + '\n'
        content += 'Engine status:\n'
        content += '\n'.join('%s: %s' % i for i in get_engine_status(self.crawler.engine))
        # print(subject)
        print(content)
        send_mail(subject=subject, content=content)
