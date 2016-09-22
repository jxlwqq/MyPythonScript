#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 下载美剧,命令行运行脚本时,必须带一个参数:剧名,第二个参数是下载类型,默认为ed2k(电驴)
# 例如:
# python download_us_drama.py 生活大爆炸 ed2k

import requests
import sys
from lxml import etree

key_words = sys.argv[1]
print '您将下载: ' + key_words
type = sys.argv[2]
print '下载类型: ' + type

type_list = ('ed2k', 'magnet')

page = 1
url = "http://cili07.com/?topic_title3=%s&p=%d" % (key_words, page)

res = requests.get(url)

tree = etree.HTML(res.text)
nodes = tree.xpath('//dl[@class="list-item"]/dd/@%s' % type)

for node in nodes:
    print node
