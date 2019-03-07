#coding=utf-8

import tools.basetornado as base 

@base.RestRouter
class Sample(base.RestBaseHandler):

    __url__ = '/api/pluginList'

    def get(self):
        self.write(base.loadKunpeng().GetPlugins())


@base.RestRouter
class PluginListPage(base.RestBaseHandler):

    __url__ = '/page/pluginList'

    def get(self):
        self.render("pluginList.html")


@base.RestRouter
class Default(base.RestBaseHandler):
    
    __url__ = '/'

    def get(self):
        self.redirect('/page/pluginList', permanent=True) 
        
