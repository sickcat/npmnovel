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
import copy
from settings import settings

class SearchHotWordHandler(tornado.web.RequestHandler):
	# get HOtword
	def get(self):
		rdata = {
			"searchHotWords": {
				"word": settings["hot_words"]
			}
		}
		rdata = {
			"searchHotWords" : settings["hot_words"]
		}
		self.write(json.dumps(rdata))
		self.set_status(200)
		self.finish()
	
	def post(self):
		pass

class AutoCompleteHandler(tornado.web.RequestHandler):
	# get auto complete key words
	def get(self):
		words = self.request.arguments["query"][0]
		words = words.split(" ")
		while '' in words:
			words.remove('')
		if len(words) == 0:
			rdata = {"keywords":settings["hot_words"]}
			self.write(json.dumps(rdata))
			self.set_status(200)
			self.finish()
			return
		if len(settings["all_books_title"]) == 0:
			books = mysql.get_all_book()
			settings["all_books_title"] = books
		else:
			books = settings["all_books_title"]
		rdata = {
			"keywords":[],
		}
		for each in books:
			for word in words:
				if word in each["title"]:
					rdata["keywords"].append(each["title"])

		if len(settings["all_chapters_title"]) == 0:
			settings["all_chapters_title"] = copy.deepcopy(mysql.get_all_chapter())
		else:
			print "redis chapters"
		chapters = settings["all_chapters_title"]
		for each in chapters:
			title = ""
			if each["title"] and "  " in each["title"]:
				title2 = each["title"][each["title"].find("  ")+2:]
				title = each["title"][:each["title"].find("  ")]
				if title2 == "":
					title2 = "  "
			else:
				title2 = "  "
			try:
				int(title[:3])
				title = title[3:]
			except Exception as e:
				pass
			for word in words:
				if word in title:
					rdata["keywords"].append(title)
				if word in title2:
					rdata["keywords"].append(title2)

		rdata["keywords"] = list(set(rdata["keywords"]))
		self.write(json.dumps(rdata))
		self.set_status(200)
		self.finish()
	
	def post(self):
		pass

class FuzzyHandler(tornado.web.RequestHandler):
	# get result
	def get(self):
		words = self.request.arguments["query"][0]
		words = words.split(" ")
		while '' in words:
			words.remove('')
		if len(words) == 0:
			rdata = {"books":[]}
			self.write(json.dumps(rdata))
			self.set_status(200)
			self.finish()
			return
		rdata = {"books":[]}
		if len(settings["all_books_title"]) == 0:
			books = mysql.get_all_book()
			settings["all_books_title"] = books
		else:
			books = settings["all_books_title"]
		for each in books:
			each["is_book"] = 1
			flag = 0
			count = -1
			for word in words:
				if word in each["title"] and each not in rdata["books"]:
					rdata["books"].append(each)
					flag = 1
			
			chapters = mysql.get_chapters_from_book(each["book_id"])
			for chapter in chapters:
				count += 1
				if chapter["click"] != 1:
					continue
				if chapter["title"] and "  " in chapter["title"]:
					title2 = chapter["title"][chapter["title"].find("  ")+2:]
					chapter["title"] = chapter["title"][:chapter["title"].find("  ")]
					if title2 == "":
						title2 = "  "
				else:
					title2 = "  "
				try:
					int(chapter["title"][:3])
					chapter["title"] = chapter["title"][3:]
				except Exception as e:
					pass
				idict = {
					"book_id": each["book_id"],
					"chapter_id": count,
					"book_title": each["title"],
					"chapter": chapter["chapter"],
					"title": chapter["title"] if chapter["title"] else chapter["chapter"],
					"title2": title2,
					"link": str(chapter["chapter_id"]),
					"click": chapter["click"],
				}
				for word in words:
					if word in chapter["title"] and idict not in rdata["books"]:
						if flag == 0:
							rdata["books"].append(each)
							flag = 1
						rdata["books"].append(idict)
					if word in title2 and idict not in rdata["books"]:
						if flag == 0:
							rdata["books"].append(each)
							flag = 1
						rdata["books"].append(idict)
		settings["hot_words"].extend(words)
		settings["hot_words"] = list(set(settings["hot_words"]))[-10:]

		'''rdata = {
			"books":[{
			"_id": 2,
			"cover": "http://www.baidu.com",
			"title": "test",
			"author": "my",
			"updated": "new",
			"cat": "",
			"tags": "",
			"longIntro": "tttttttt",
			"lastChapter": "123",
			"is_book": 1,
			},
			{
			"chapter": "abc",
			#"index": each["chapter_id"],
			"title": "title1",
			"title2": "title2",
			"link": str("1"),
			"click": 12,
			"is_book": 0,
			}],
		}'''
		self.write(json.dumps(rdata))
		self.set_status(200)
		self.finish()
	
	def post(self):
		pass
