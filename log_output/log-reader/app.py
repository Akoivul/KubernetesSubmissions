import signal
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


def read(path, default=""):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        return default


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"{read('/files/log.txt')}\nPing / Pongs: {read('/files/pingpong.txt', '0')}"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body.encode())


signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

HTTPServer(("0.0.0.0", 3000), Handler).serve_forever()