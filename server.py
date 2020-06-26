#!/usr/bin/python3

import http.server
import socketserver
import os

# Default port
PORT = 80

# Changes default folder to www/
web_dir = os.path.join(os.path.dirname(__file__), 'www')
os.chdir(web_dir)

# Starts server
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving http://localhost/ at port", PORT)
    httpd.serve_forever()