# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import tornado
import mysqlDb.mysql as mysql
import time
import json
# /buy/cinemaid_showinid_movieid
class BookHandler(tornado.web.RequestHandler):
	
	def get(self, URL):
		#get book from id
		#todo 1.get id
		book_id = URL
		
		rdata = {
			"_id": 1,
			"cover": "http://www.baidu.com",
			"title": "test",
			"author": "my",
			"updated": "new",
			"cat": "",
			"tags": "",
			"longIntro": "tttttttt",
		}
		self.write(json.dumps(rdata))
		self.finish()
	
	def post(self, URL):
		pass

class BookViewHandler(tornado.web.RequestHandler):
	
	def get(self, URL=""):
		#get book from id
		#todo 1.get id
		book_id = URL
		
		rdata = [{"book":{
			"_id": 1,
			"cover": "http://www.baidu.com",
			"title": "test",
			"author": "my",
			"updated": "new",
			"cat": "",
			"tags": "",
			"longIntro": "tttttttt",
			"lastChapter": "123",
			}, "index":1},
			{"book":{
			"_id": 2,
			"cover": "http://www.baidu.com",
			"title": "test2",
			"author": "my2",
			"updated": "new2",
			"cat": "2",
			"tags": "2",
			"longIntro": "2tttttttt",
			"lastChapter": "2123",
			}, "index":2}]
		rdata = [
			{
			"_id": 1,
			"cover": "http://www.baidu.com",
			"title": "test",
			"author": "my",
			"updated": "new",
			"cat": "",
			"tags": "",
			"longIntro": "tttttttt",
			"lastChapter": "123",
			},
			{
			"_id": 2,
			"cover": "http://www.baidu.com",
			"title": "test",
			"author": "my",
			"updated": "new",
			"cat": "",
			"tags": "",
			"longIntro": "tttttttt",
			"lastChapter": "123",
			},
		]
		self.write(json.dumps(rdata))
		self.finish()
	
	def post(self, URL):
		pass