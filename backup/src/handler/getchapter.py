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

class ChapterHandler(tornado.web.RequestHandler):
	# get chapters
	def get(self, URL):
		#chapter from book_id
		#todo 1.get id
		#rdata = {
		#	"chapters":[
		#		{"chapter":"diyi", "index": 1, "title":"aaa", "link":"1"},
		#		{"chapter":"dier", "index": 2, "title":"bbb", "link":"2"},
		#		{"chapter":"disa", "index": 3, "title":"CCC", "link":"3"},
		#		]
		#}
		
		book_id = int(URL)
		chapters = mysql.get_chapters_from_book(book_id)

		#mulu = open(os.path.join(settings["data_path"], str(book_id), "目录.txt"), "rb")
		#mulusets = {}
		#count = 0
		#if mulu:
		#	for each in mulu.readlines():
		#		mulusets[each[:-2].decode('gb2312')] = count;
		#		count += 1

		#print mulusets.keys()
		
		rdata = {"chapters":[]}
		for each in chapters:
			if each["title"] and "  " in each["title"]:
				title2 = each["title"][each["title"].find("  ")+2:]
				each["title"] = each["title"][:each["title"].find("  ")]
				if title2 == "":
					title2 = "  "
			else:
				title2 = "  "

			try:
				int(each["title"][:3])
				each["title"] = each["title"][3:]
			except Exception as e:
				pass

			idict = {
				"chapter": each["chapter"],
				#"index": each["chapter_id"],
				"title": each["title"] if each["title"] else each["chapter"],
				"title2": title2,
				"link": str(each["chapter_id"]),
				#"value": 100 if each["title"] not in mulusets.keys() else mulusets[each["title"]],
			}
			rdata["chapters"].append(idict)

		#sorted(rdata["chapters"], key=lambda i: i["value"])
		self.write(json.dumps(rdata))
		self.set_status(200)
		self.finish()
	
	def post(self):
		pass

class GetChapterHandler(tornado.web.RequestHandler):

	#rdata = {
	#		"title": "test title",
	#		"chapter": {
	#			"body": """
	#			testbody
	#			""",
	#			"title": "test",
	#		},
	#	}
	def get(self, URL = ""):
		#get chapter detail
		chapter_id = int(self.request.arguments["chapterUrl"][0])
		chapter = mysql.get_chapter_from_id(chapter_id)[0]
		book = mysql.get_book_from_id(int(chapter['book_id']))[0]
		mysql.add_click(book["book_id"])
		mysql.add_read(book["book_id"])
		f = open(os.path.join(settings["data_path"], str(book["book_id"]), chapter["link"]))
		body = f.read()
		rdata = {
			"title": book["title"],
			"chapter": {
				"body": body,
				"title": chapter["title"],
			}
		}
		self.write(json.dumps(rdata))
		self.finish()