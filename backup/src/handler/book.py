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
		book = mysql.get_book_from_id(int(book_id))
		if len(book) == 0:
			self.set_status(404)
			self.finish()
			return
		book = book[0]
		rdata = {
			"_id": book["book_id"],
			"cover": book["cover"],
			"title": book["title"],
			"updated": book["updated"],
			"cat": book["cat"],
			"tags": book["tags"],
			"longIntro": book["longintro"],
		}
		self.write(json.dumps(rdata))
		self.finish()
	
	def post(self, URL):
		pass

#/api/book?view=updated
class BookViewHandler(tornado.web.RequestHandler):
	
	def get(self, URL=""):
		#get book from id
		#todo 1.get id
		book_id = URL
		ids = self.request.arguments["id"][0]
		rdata = []
		for each in ids.split(","):
			if each == "":
				continue
			book = mysql.get_book_from_id(int(each))[0]
			idict = {
				"_id":book["book_id"],
				"cover": book["cover"],
				"title": book["title"],
				"updated": book["updated"],
				"cat": book["cat"],
				"tags": book["tags"],
				"longIntro": book["longintro"],
				"lastChapter": book["last_chapter"],
				"author": book["author"],
			}
			rdata.append(idict)
		self.write(json.dumps(rdata))
		self.finish()
		return
		'''
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
		'''
	
	def post(self, URL):
		pass