import os
import signal
import sys
import threading
import time
import uuid
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = int(os.environ.get("PORT", 3000))
RANDOM_STRING = str(uuid.uuid4())

def timestamp():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(f"{timestamp()}: {RANDOM_STRING}".encode())


signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

threading.Thread(target=HTTPServer(("0.0.0.0", PORT), Handler).serve_forever, daemon=True).start()

while True:
    print(f"{timestamp()}: {RANDOM_STRING}", flush=True)
    time.sleep(5)