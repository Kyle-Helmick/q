#!/usr/bin/python

import os
import cgi
import urllib

def br():
    print '<br>'

def p(s):
    print "<p>%s</p>" % s
#cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print('')
br()
print 'Request Method: ' + os.environ['REQUEST_METHOD']
br()
print 'Rsrc requested: ' + os.environ['PATH_INFO']
br()

p('Query: ' + urllib.unquote(os.environ['QUERY_STRING']))

cgi.print_environ()
