import os
import signal
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 3000))
counter = 0


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        global counter
        if self.path != "/pingpong":
            self.send_error(404)
            return
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"pong {counter}".encode())
        counter += 1
        with open("/files/pingpong.txt", "w") as f:
            f.write(str(counter))


signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

print(f"Server started in port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()