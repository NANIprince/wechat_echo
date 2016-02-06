import sae
import urlparse
import hashlib

def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/html: charset=utf-8')]
    start_response(status, response_headers)
    query=environ["QUERY_STRING"]
    echostr=urlparse.parse_qs(query)['echostr']
    return echostr

application = sae.create_wsgi_app(app)