#coding=utf-8

import tools.basetornado as base 

@base.RestRouter
class Scan(base.RestBaseHandler):

    __url__ = '/page/scanItem'

    def get(self):
        self.render("scan.html")

    def post(self):
        kp = base.loadKunpeng()
        code = self.xArguments("code")[0]
        kp.StartBuffer()
        message = kp.Check(code)
        log = kp.BufferContent("")
        self.render("result.html",result=message,log=log)


