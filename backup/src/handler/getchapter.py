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
class ChapterHandler(tornado.web.RequestHandler):
	
	def get(self, URL):
		#get book from id
		#todo 1.get id
		
		print self.request.uri
		rdata = {
			"chapters":[
				{"chapter":"diyi", "index": 1, "title":"aaa", "link":"1"},
				{"chapter":"dier", "index": 2, "title":"bbb", "link":"2"},
				{"chapter":"disa", "index": 3, "title":"CCC", "link":"3"},
				]
		}
		self.write(json.dumps(rdata))
		self.set_status(200)
		self.finish()
	
	def post(self):
		pass

class GetChapterHandler(tornado.web.RequestHandler):

	def get(self, URL = ""):
		print self.request.uri
		rdata = {
			"title": "test",
			"chapter": {
				"body": "asdfasdfa",
				"title": "test",
			},
		}
		self.write(json.dumps(rdata))
		self.finish()