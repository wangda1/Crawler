#-*-coding:utf-8-*-
#This page is for analysis of the page
#2017.3.31.N

from selenium import webdriver
import time
from bs4 import BeautifulSoup
import re

class Page:
    def __init__(self,url,num,save_addr):
        self.url=url
        self.num=num
        self.file_name=file_name

class Sele:
    def __init__(self,url,num,file_name,keywords):
        self.url=url
        self.num=num
        self.file_name=file_name
        self.keywords=keywords

    def Download(self):
        firefox = webdriver.Firefox()
        firefox.get('url')
        for i in range(1,6):
            s="window.scrollTo(0,(document.body.scrollHeight/{0})*{1});".format(6,i)
            firefox.execute_script(s)
            time.sleep(2)
        with open("'self.file_name'.html",'w',encoding='utf8')as f:
            f.write(firefox.page_source)


#豆瓣短评链接格式:https://movie.douban.com/subject/25900945/comments?status=P
#豆瓣问题链接格式:https://movie.douban.com/subject/25900945/questions/?from=subject
#豆瓣影评链接格式:https://movie.douban.com/subject/25900945/reviews
#
#
class Douban_parse(Sele):
    def __init__(self,num,file_name):
        self.num=num
        self.file=file_name

    def parse(self):
        re_comm

    def Download(self):
        firefox = webdriver.Firefox()

        with open("'self.file_name'.html",'r',encoding='utf8')as f:
            bs = BeautifulSoup(f.read())
                       
    

































































