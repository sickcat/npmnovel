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
		
		rdata = {
			"books":[
				{
				"_id": 1,
				"cover": "",
				"title": "test",
				"author": "my",
				"updated": "new",
				"cat": "",
				"tags": "",
				"longIntro": "tttttttt",
				}
			]
		}
		self.write(json.dumps(rdata))
		self.set_status(200)
		self.finish()
	
	def post(self):
		pass