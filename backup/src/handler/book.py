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
		chaptername = mysql.get_chapter_from_id(book["last_chapter"])[0]["title"]
		mysql.add_click(book_id)
		rdata = {
			"_id": book["book_id"],
			"cover": book["cover"],
			"title": book["title"],
			"updated": book["updated"],
			"cat": book["cat"],
			"tags": book["tags"],
			"longIntro": book["longintro"],
			"author": book["author"],
			"read_count": book["read_count"],
			"lastChapter": chaptername,
			"wordCount": book["word_count"],
			"click_count": book["click_count"],
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
			if each == "" or each == "undefined":
				continue
			book = mysql.get_book_from_id(int(each))[0]
			chaptername = mysql.get_chapter_from_id(book["last_chapter"])[0]["title"]
			idict = {
				"_id":book["book_id"],
				"cover": book["cover"],
				"title": book["title"],
				"updated": book["updated"],
				"cat": book["cat"],
				"tags": book["tags"],
				"longIntro": book["longintro"],
				"lastChapter": chaptername,
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