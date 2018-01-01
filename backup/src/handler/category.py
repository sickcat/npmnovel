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
class CategoryHandler(tornado.web.RequestHandler):
	
	def get(self):
		#get book from id
		#todo 1.get id
		#get books
		#rdata = {
		#	"books":[
		#		{
		#		"_id": 1,
		#		"cover": "",
		#		"title": "test",
		#		"author": "my",
		#		"updated": "new",
		#		"cat": "",
		#		"tags": "1 2 3",
		#		"longIntro": "tttttttt",
		#		}
		#	]
		#}
		books = mysql.get_all_book()
		rdata = {
			"books": [
			]
		}
		for each in books:
			idict = {
				"_id": each["book_id"],
				"cover": each["cover"],
				"title": each["title"],
				"updated": each["updated"],
				"cat": each["cat"],
				"tags": each["tags"],
				"shortIntro": each["shortintro"],
				"longIntro": each["longintro"],
				"author": each["author"],
			}
			rdata["books"].append(idict)
		self.write(json.dumps(rdata))
		self.set_status(200)
		self.finish()
	
	def post(self):
		pass