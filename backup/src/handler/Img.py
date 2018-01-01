# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import tornado
import os
from settings import settings

# noinspection PyAbstractClass
class ImgHandler(tornado.web.RequestHandler):

    def get(self):
    	path = self.request.arguments["path"][0]
    	img_path = os.path.join(settings["data_path"], path)
    	f = open(img_path)
    	img = f.read()
    	self.write(img)
    	self.set_header("Content-type", "image/png")
        self.finish()

    def post(self):
    	self.write('test post')
    def put(self):
    	self.write('test put')
