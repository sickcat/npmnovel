# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#from handler.getData.foo import FooHandler
from handler.book import BookHandler
from handler.book import BookViewHandler
from handler.category import CategoryHandler
from handler.getchapter import ChapterHandler
from handler.getchapter import GetChapterHandler
from handler.Img import ImgHandler
from handler.types import TypesHandler
from handler.oms import GetBooksHandler
from handler.oms import UpdateBooksHandler, ZipHandler
from handler.search import SearchHotWordHandler, AutoCompleteHandler
from handler.search import FuzzyHandler
url_patterns = [

    #Test server
    #(r"/foo", FooHandler),
    (r'/api/book', BookViewHandler),
    (r'/api/book/(\w+)', BookHandler),
    (r'/category', CategoryHandler),
    (r'/category/detail', CategoryHandler),
    (r'/api/category/detail', CategoryHandler),
    (r'/api/chapters/(\w+)', ChapterHandler),
    (r'/api/getChapter', GetChapterHandler),
    (r'/api/img', ImgHandler),
    (r'/api/types', TypesHandler),
    
    (r'/oms/books', GetBooksHandler),
    (r'/oms/book/(\w+)', UpdateBooksHandler),
    (r'/oms/zip', ZipHandler),
    (r'/api/book/search-hotwords', SearchHotWordHandler),
    (r'/api/book/auto-complete', AutoCompleteHandler),
    (r'/api/book/search-hotwords/fuzzy', FuzzyHandler)
    #(r'/index/(\w+)', MainHandler),
    #(r'/index', MainHandler),
    #(r'/movie/(\w+)', MovieHandler),
    #(r'/buy/(\w+)', BuyHandler),
    #(r'/register', RegisterHandler),
    #(r'/login', LoginHandler),
    #(r'/logout', LogoutHandler),
    #(r'/order', OrderHandler),
    #(r'.*', IndexHandler),

]
