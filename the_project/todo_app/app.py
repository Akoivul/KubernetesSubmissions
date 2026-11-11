import html
import json
import os
import signal
import sys
import time
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 3000))
BACKEND = "http://todo-backend-svc:2345/todos"
IMAGE = "/files/image.jpg"
MAX_AGE = 600

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
    if os.path.exists(IMAGE) and time.time() - os.path.getmtime(IMAGE) < MAX_AGE:
        return
    try:
        urllib.request.urlretrieve("https://picsum.photos/1200", IMAGE + ".tmp")
        os.replace(IMAGE + ".tmp", IMAGE)
    except Exception as e:
        print(f"Could not fetch a new image: {e}", flush=True)


def get_todos():
    try:
        with urllib.request.urlopen(BACKEND) as r:
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
            with open(IMAGE, "rb") as f:
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
