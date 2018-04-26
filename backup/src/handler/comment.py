# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import tornado
import torndb
from datetime import datetime
import mysqlDb.mysql as mysql
import time
import json
# /buy/cinemaid_showinid_movieid
class GetCommentHandler(tornado.web.RequestHandler):
	
	def get(self, url):
		print url
		sql = 'select * from Comment where book_id={0}'.format(url)
		cdata = mysql.database(0, sql)
		comment = []
		for each in cdata:
			if each["to_id"] == 0:
				idict = {
					"id": each["id"],
					"name": each["name"],
					"time": each["time"][0:10],
					"content": each["content"],
					"reply":[],
				}
				comment.append(idict)
			else:
				for each2 in comment:
					if len(each2["reply"]) == 0:
						if each2["id"] == each["to_id"]:
							idict = {
								"id": each["id"],
								"responder": each["name"],
								"reviewers": each["to_name"],
								"time": each["time"][0:10],
								"content": each["content"],
							}
							each2["reply"].append(idict)
					else:
						for each3 in each2["reply"]:
							if each3["id"] == each["to_id"]:
								idict = {
									"id": each["id"],
									"responder": each["name"],
									"reviewers": each["to_name"],
									"time": each["time"][0:10],
									"content": each["content"],
								}
								each2["reply"].append(idict)

		rdata = {
			"comment": comment,
		}
		self.write(json.dumps(rdata))
		self.set_status(200)
		self.finish()

class PostCommentHandler(tornado.web.RequestHandler):
	def post(self, URL):
		print URL
		data = json.loads(self.request.body)
		print data
		name = torndb.MySQLdb.escape_string(str(data["name"]))
		content = torndb.MySQLdb.escape_string(str(data["content"]))
		rtype = int(data["rtype"])
		replyid = int(data["replyid"])
		if rtype == 0:
			replyid = 0
		sql = 'select * from Comment where id={0}'.format(replyid)
		reply_name = mysql.database(0, sql)
		if reply_name:
			reply_name = reply_name[0]["name"]
		else:
			reply_name = ""
		nowtime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		sql = 'INSERT INTO Comment(`time`, content, name, to_id, to_name, book_id) VALUES("{0}", "{1}", "{2}", {3}, "{4}", {5})'.format(
			nowtime, content, name, replyid, torndb.MySQLdb.escape_string(str(reply_name)), int(URL))
		mysql.database(1, sql)
		
		self.write("success")
		self.finish()
