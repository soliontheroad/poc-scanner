#coding=utf-8

from config import * 
import tools.basetornado as base 

@base.RestRouter
class Message(base.RestBaseHandler):

    __url__ = '/page/message'


    def get(self):
        self.render("message.html")


