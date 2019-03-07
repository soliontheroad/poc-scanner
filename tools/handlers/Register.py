#coding=utf-8

from config import * 
import tools.basetornado as base 
import random
import json
import hashlib

def json_plugin_file(json_plugin):
    m = hashlib.md5()
    m.update(json_plugin["meta"]["name"].encode("utf-8"))
    n = m.hexdigest()
    return "ugj_%s.json" % (n)

def randomString(l):
    """ 
    Make an random password.
    """
    charlist = "abcdefghijkmnpqrstuvwxyz12345678_ABCDEFGHIJKMNPQRSTUVWXYZ"
    r = []
    for i in range(0,l):
        c = random.sample(charlist,1)
        r.append("".join(c))
    return "".join(r)



@base.RestRouter
class Register(base.RestBaseHandler):

    __url__ = '/page/registerPlugin'


    def get(self):
        self.render("register.html")

    def post(self):
        code = self.xArguments("code")
        json_plugin = json.loads(code[0])
        f_name = randomString(24) + ".json"

        json_plugin["meta"]["name"] = "[user:%s]" % (json_plugin["meta"]["name"])
        ugj_filename = "%s/%s" % (EXTRA_PATH,json_plugin_file(json_plugin))

        if json_plugin['target'] == "" or json_plugin['meta']['name'] == "" or json_plugin['meta']['type'] == "" :
            self.render("message.html",message="target,meta.name,meta.type 不能为空!请重新添加!",next="/page/registerPlugin")
        else:
            open(ugj_filename,"w").write(json.dumps(json_plugin,sort_keys=True, indent=4, separators=(',', ':')))
            self.render("message.html",message="添加成功!",next="/")



