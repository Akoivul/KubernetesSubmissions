import os
import signal
import sys
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer


def read_log():
    try:
        with open("/files/log.txt") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def read_info():
    with open("/config/information.txt") as f:
        return f.read().strip()


def get_pings():
    try:
        with urllib.request.urlopen("http://ping-pong-svc:2346/pings") as r:
            return r.read().decode()
    except Exception:
        return "unavailable"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = (
            f"file content: {read_info()}\n"
            f"env variable: MESSAGE={os.environ.get('MESSAGE')}\n"
            f"{read_log()}\nPing / Pongs: {get_pings()}"
        )
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body.encode())


signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

HTTPServer(("0.0.0.0", 3000), Handler).serve_forever()