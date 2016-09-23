#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from lxml import etree
imdb_url = 'http://www.imdb.com/chart/top/'

res = requests.get(imdb_url)
tree = etree.HTML(res.text)
nodes = tree.xpath('//td[@class="titleColumn"]/a')
for node in nodes:
    print node.text


