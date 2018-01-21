# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import tornado
import mysqlDb.mysql as mysql
import time
import json
import os
from settings import settings

class SearchHotWordHandler(tornado.web.RequestHandler):
	# get HOtword
	def get(self):
		rdata = {
			"searchHotWords": {
				"word": [
					"aaa",
					"bbb",
				]
			}
		}
		self.write(json.dumps(rdata))
		self.set_status(200)
		self.finish()
	
	def post(self):
		pass
