# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:38:34 2018

@author: LI
"""

from __future__ import print_function
from urllib.request import urlopen
from bs4 import BeautifulSoup #BeautifulSoup将html解析为对象进行处理，全部页面转变为字典或者数组，相对于正则表达式的方式，可以大大简化处理过程。
import re #正则表达式模块



Year_Start = 2000
Year_End   = 2003
base_url     ='https://www.federalreserve.gov'


'''
以下代码功能：得到Minutes的链接
'''
links = []
for year in range(Year_Start, Year_End+1):
    fomc_url = base_url + '/monetarypolicy/fomchistorical' + str(year) + '.htm'
    fomc_socket = urlopen(fomc_url) # urllib.urlopen(url[, data[, proxies]])创建一个表示远程url的类文件对象，然后像本地文件一样操作这个类文件对象来获取远程数据。
    soup = BeautifulSoup(fomc_socket, 'html.parser')# BeautifulSoup默认支持Python的标准HTML解析库（使用方法：BeautifulSoup(html,’html.parser’)），它也支持一些第三方的解析库（略）
    statements = soup.find_all('a', href=re.compile('\A/fomc/minutes/\d{8}.htm\Z'),text = 'Minutes')
    # find_all() 方法搜索当前tag的所有tag子节点，并判断是否符合过滤器的条件 http://blog.csdn.net/depers15/article/details/51934210 
    # 关于^A^Z的解释 http://blog.csdn.net/justheretobe/article/details/53152267
    links.append([statement.attrs['href'] for statement in statements])
    #statement.attrs['href']返回的是一个属性字典，是BeautifulSoup中为对象定义的一个方法。以<a href="http://www.baidu.com" title="Yes me">Baidu</a>为例，{'href': 'http://www.baidu.com', 'title': 'Yes me' }




def get_articles(links):
    articles = links
    for index1 in range(len(links)):
        for index2 in range(len(links[index1])):
            statement_socket = urlopen(base_url + links[index1][index2])
            statement = BeautifulSoup(statement_socket, 'html.parser')
            paragraphs = statement.findAll('p')
            links[index1][index2] =  "\n\n".join([paragraph.get_text().strip() for paragraph in paragraphs])
    return articles #实际上返回的是articles
            
articles = get_articles(links)