#!/usr/bin/python

import os
import cgi

def br():
    print '<br>'


#cgitb.enable()

print("Content-Type: text/html;charset=utf-8")
print('')
print("Hello World!")
br()
print 'Request Method: ' + os.environ['REQUEST_METHOD']
br()
print 'Rsrc requested: ' + os.environ['PATH_INFO']
br()

cgi.print_environ()
