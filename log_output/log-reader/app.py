import signal
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        with open("/files/log.txt", "rb") as f:
            self.wfile.write(f.read())


signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

HTTPServer(("0.0.0.0", 3000), Handler).serve_forever()