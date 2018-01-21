# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import tornado
import torndb
import mysqlDb.mysql as mysql
import time
from datetime import datetime
from script import otk
from settings import settings
import os
# get /oms/books
class GetBooksHandler(tornado.web.RequestHandler):
	
	# 获取所有书本，包括删除的
	# 渲染页面
	# book-list
	# add book	
	def get(self):
		#read movies and cinemas etc
		#cinema
		'''user_id = self.get_cookie('UserId')
								print user_id
								username = mysql.get_user_info(user_id)
								res = URL.split('_')
						
								if len(res) != 3: #argument not match
									self.redirect('/')
								
								movie_detail = mysql.get_movie(res[2])[0]
								showin_detail = mysql.get_showin(res[1])[0]
								seat_list = str(showin_detail['seat']).split(',')
								self.render('buy.html', cookieName = username, movie = movie_detail,
									alert = alert, alert_msg = alert_msg,seat_list = seat_list,
									cinema_id = res[0], showin_id = res[1], flag = 1)
						'''
		sql = 'SELECT * FROM Book'
		books = mysql.database(0, sql)
		self.render('books.html', books = books)

# /oms/book/book_id
class UpdateBooksHandler(tornado.web.RequestHandler):

	#获得书本
	def get(self, URL):
		print URL
		if URL == "undefined":
			book = {
				"title": "",
				"book_id": "undefined",
				"cover": "",
				"word_count": "",
				"longintro": "",
				"shortintro": "",
				"deleted": 2,
				"author": "",
				"updated": "",
			}
			self.render('book.html', book = book)
			return

		sql = 'select * from Book where book_id={0}'.format(URL)
		book = mysql.database(0, sql)[0]

		self.render('book.html', book = book)

	#增加书本
	def post(self, URL):
		print URL
		title = torndb.MySQLdb.escape_string(self.request.arguments["title"][0])
		author = torndb.MySQLdb.escape_string(self.request.arguments["author"][0])
		word_count = int(self.request.arguments["word_count"][0])
		longintro = torndb.MySQLdb.escape_string(self.request.arguments["longintro"][0])
		shortintro = torndb.MySQLdb.escape_string(self.request.arguments["shortintro"][0])
		deleted = int(self.request.arguments["deleted"][0])
		update_time = self.request.arguments["updated"][0]
		msg = ""
		if URL == 'undefined':
			sql = 'SELECT MAX(book_id) from Book'
			book_id = mysql.database(0, sql)[0]["MAX(book_id)"] + 1
			sql = 'INSERT INTO Book(book_id, cover, title, updated, cat, tags, read_count, word_count, longintro, author, shortintro, deleted) VALUES({0}, "", "{1}", "{2}", "", "", 0, {3}, "{4}", "{5}", "{6}", {7})'.format(
				book_id, title, update_time, word_count, longintro, author, shortintro, deleted)
		else:
			sql = 'UPDATE Book set title="{0}", author="{1}", word_count={2}, longintro="{3}", shortintro="{4}", deleted={5}, updated="{7}" where book_id={6}'.format(
				title, author, word_count, longintro, shortintro, deleted, URL, update_time)
		mysql.database(1, sql)
		settings["all_books_title"] = []
		settings["all_chapters_title"] = []
		self.write("success")
		self.finish()

# /oms/zip/URL
class ZipHandler(tornado.web.RequestHandler):

	#接收上传的zip文件夹,并调用更新脚本
	def post(self, URL=""):
		settings["all_books_title"] = []
		settings["all_chapters_title"] = []
		book_id = int(self.request.arguments["book_id"][0])
		f = self.request.files.get('fileUpload')
		sql = 'SELECT * FROM Book WHERE book_id={0}'.format(book_id)
		book = mysql.database(0, sql)
		if not f or not book or book[0]["deleted"] != 2:
			self.write("no file!")
			self.finish()
		f = f[0]
		file_path=os.path.join(settings["data_path"], "tmp", f["filename"])
		with open(file_path, "wb") as f2:
			f2.write(f['body'])
		otk(file_path, book_id)
		self.write("success")
		self.finish()

