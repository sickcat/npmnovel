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
import sys
import torndb
from settings import settings

import zipfile
from bs4 import BeautifulSoup

database = mysql.database
# 整个流程
def otk(file_path, book_id="tmp"):
	# 验证数据库记录
	sql = 'SELECT * FROM Book where book_id={0}'.format(book_id)
	book = database(0, sql)
	if len(book) == 0:
		return -1
	
	# 解压缩
	if not os.path.exists(os.path.join(settings["data_path"], str(book_id))):
		os.mkdir(os.path.join(settings["data_path"], str(book_id)))
	rezip(file_path, book_id)
	
	# 解压后先插入图片，确定数据库是否存在正确的记录，deleted=2才可插入！
	cover_name = ""
	for each in os.listdir(os.path.join(settings["data_path"], str(book_id))):
		if "title" in each:
			cover_name = each
	sql = 'UPDATE Book SET cover="{0}" where book_id={1}'.format(
		str(book_id) + "/" + cover_name, book_id)
	database(1, sql)
	
	#生成html文件
	word_path = os.path.join(settings["data_path"], str(book_id), "word")
	abiword(word_path)
	#更换img源
	update_img_src(word_path, book_id)

	for each in os.listdir(word_path):
		if each.split(".")[-1] == "html":
			size = os.path.getsize(os.path.join(word_path, each))
			sql = "select max(chapter_id) from Chapter"
			chapter_id = database(0, sql)[0]["max(chapter_id)"] + 1
			sql = 'INSERT INTO Chapter(chapter_id, chapter, book_id, title, link, read_count, word_count) VALUES({0},"{1}", {2}, "{3}", "{4}", 0, {5})'.format(
				chapter_id, torndb.MySQLdb.escape_string(each[:-5]), book_id, torndb.MySQLdb.escape_string(each[:-5]), torndb.MySQLdb.escape_string('word/' + each), int(float(size)/18))
			database(1, sql)

# 输入解压文件位置
# 解压文件要求结构： 只包含word文件夹和title图片
def rezip(file_path, book_id="tmp"):
	f = zipfile.ZipFile(file_path, 'r')
	for file in f.namelist():
		f.extract(file, os.path.join(settings["data_path"], str(book_id)))

def abiword(path):
	# 调用abiword软件，从doc和docx生成html
	os.system("cd " + path + " && abiword --to=html *.doc && abiword --to=html *.docx")

def update_img_src(path, book_id="tmp"):
	# 更换所有img标签的src属性
	# 原： dct12.html_files/1.png
	# /api/img?path= bookid/chaptername.html_files/1.png
	for each in os.listdir(path):
		if each.split(".")[-1] == "html":
			f = open(os.path.join(path, each), "r")
			soup = BeautifulSoup(f.read())
			f.close()
			for img in soup.find_all("img"):
				img["src"] = "/api/img?path=" + str(book_id) + "/word/" + img["src"]
			f = open(os.path.join(path, each), "w")
			f.write(soup.prettify())
			f.close()

if __name__ == "__main__":
	otk("/home/bm/规范.zip", 4)