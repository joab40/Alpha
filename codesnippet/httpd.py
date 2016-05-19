import SimpleHTTPServer
import SocketServer
import os

# Set httpd root
os.chdir("../share/images/model")

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
