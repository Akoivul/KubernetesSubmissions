import json
import os
import signal
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

PORT = int(os.environ.get("PORT", 3000))
todos = []


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/todos":
            self.send_error(404)
            return
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(todos).encode())

    def do_POST(self):
        if self.path != "/todos":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0))
        todo = parse_qs(self.rfile.read(length).decode()).get("todo", [""])[0].strip()
        if todo and len(todo) <= 140:
            todos.append(todo)
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()


signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

print(f"Server started in port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
