import html
import json
import os
import signal
import sys
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ["PORT"])
BACKEND_URL = os.environ["BACKEND_URL"]
IMAGE_URL = os.environ["IMAGE_URL"]
IMAGE_PATH = os.environ["IMAGE_PATH"]
IMAGE_MAX_AGE = int(os.environ["IMAGE_MAX_AGE"])

HTML = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Todo app</title>
  </head>
  <body>
    <h1>Todo app</h1>
    <img src="/image" width="600">
    <form method="post" action="/todos">
      <input type="text" name="todo" maxlength="140">
      <button type="submit">Send</button>
    </form>
    <ul>
{todos}
    </ul>
  </body>
</html>
"""


def refresh_image():
    if os.path.exists(IMAGE_PATH) and time.time() - os.path.getmtime(IMAGE_PATH) < IMAGE_MAX_AGE:
        return
    try:
        urllib.request.urlretrieve(IMAGE_URL, IMAGE_PATH + ".tmp")
        os.replace(IMAGE_PATH + ".tmp", IMAGE_PATH)
    except Exception as e:
        print(f"Could not fetch a new image: {e}", flush=True)


def get_todos():
    try:
        with urllib.request.urlopen(BACKEND_URL) as r:
            return json.load(r)
    except Exception as e:
        print(f"Could not fetch todos: {e}", flush=True)
        return []


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            refresh_image()
            items = "".join(f"<li>{html.escape(t)}</li>" for t in get_todos())
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(HTML.replace("{todos}", items).encode())
        elif self.path == "/image":
            with open(IMAGE_PATH, "rb") as f:
                data = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "image/jpeg")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)
        else:
            self.send_error(404)


signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

print(f"Server started in port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
