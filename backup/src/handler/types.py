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
class TypesHandler(tornado.web.RequestHandler):
	
	def get(self):
		#types: [{
        #        type: 'all',
        #        name: '全部'
        #    },{
        #        type: ''
        #    }]
		cats = mysql.get_all_cats()
		rdata = []
		for each in cats:
			idict = {
				"type": each["cat_id"],
				"name": each["name"],
			}
			rdata.append(idict)
		self.write(json.dumps(rdata))
		self.set_status(200)
		self.finish()
	
	def post(self):
		pass