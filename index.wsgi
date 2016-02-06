import os

import sae
import hashlib
import web

urls = (
    '/', 'wechat'
)



class echo:
    def GET(self):
    	data = web.import()
    	echostr = data.echostr
        return echostr


app = web.application(urls, globals()).wsgifunc()

application = sae.create_wsgi_app(app)