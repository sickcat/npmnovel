from settings import settings
import torndb
import json
import time

def database(fun, sql):
	try:
		db = torndb.Connection(host=settings["host"],
			database=settings['database'],
			user=settings["user"],
			password=settings["password"],
			time_zone=settings["timezone"])
		if fun == 0:
			return db.query(sql)
		else:
			db.execute(sql)
			return None
	except Exception as e:
		print sql
		print e
		print "-----------Connect Error Try Again..."

def add_click(book_id):
	sql = 'update Book set click_count = click_count + 1 where book_id={0}'.format(book_id)
	database(1, sql)

def add_read(book_id):
	sql = 'update Book set read_count = read_count + 1 where book_id={0}'.format(book_id)
	database(1, sql)

#only use in this file to check digit
def isDigit(_input):
	if not _input:
		return False
	if not str(_input).isdigit():
		return False
	return True

#index.py -> [IndexHandler]
def get_cinema_list():
	sql = 'select * from cinema'
	return database(0, sql)


#book.py -> [BookHandler]
def get_book_from_id(book_id):
	sql = 'select * from Book where book_id={0} and deleted != 1'.format(int(book_id))
	return database(0, sql)

#category.py -> [CategoryHandler]
def get_all_book(book_type = ""):
	sql = 'select * from Book where deleted != 1'
	return database(0, sql)

#getchapter.py -> [ChapterHandler]
def get_chapters_from_book(book_id):
	sql = 'select * from Chapter where book_id={0} and deleted != 1'.format(int(book_id))
	return database(0, sql)

def get_chapter_from_id(chapter_id):
	sql = 'select * from Chapter where chapter_id={0} and deleted != 1'.format(chapter_id)
	return database(0, sql)

def get_all_cats():
	sql = 'select * from Cat'
	return database(0, sql)

def get_all_chapter():
	sql = 'select * from Chapter where book_id in (select book_id from Book where deleted != 1) and deleted!=1'
	return database(0, sql)

def update_user_book(user_id, book_id):
	sql = 'select * from User where user_id="{0}"'.format(torndb.MySQLdb.escape_string(user_id))
	user = database(0, sql)
	#new user
	if len(user) == 0:
		sql = 'insert into User(user_id, read_list) Values("{0}", "{1}")'.format(
			torndb.MySQLdb.escape_string(user_id), str(book_id))
		database(1, sql)
	else:
		read_list = user[0]["read_list"].split(',')
		read_list.append(str(book_id))
		read_list = list(set(read_list))
		read_list = ','.join(read_list)
		sql = 'update User set read_list="{0}" where user_id="{1}"'.format(
			read_list, torndb.MySQLdb.escape_string(user_id))
		database(1, sql)

def get_read_list(user_id):
	sql = 'select * from User where user_id="{0}"'.format(torndb.MySQLdb.escape_string(user_id))
	rlist = database(0, sql)
	if rlist:
		return rlist[0]["read_list"].split(',')
	else:
		return []