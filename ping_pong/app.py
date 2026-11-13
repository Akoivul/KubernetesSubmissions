import os
import signal
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

import psycopg

PORT = int(os.environ.get("PORT", 3000))
DATABASE_URL = os.environ["DATABASE_URL"]


def query(sql):
    with psycopg.connect(DATABASE_URL, autocommit=True) as conn:
        cur = conn.execute(sql)
        return cur.fetchone() if cur.description else None


def init_db():
    while True:
        try:
            query("CREATE TABLE IF NOT EXISTS counter (id INT PRIMARY KEY, value INT)")
            query("INSERT INTO counter VALUES (1, 0) ON CONFLICT DO NOTHING")
            return
        except psycopg.OperationalError as e:
            print(f"Waiting for database: {e}", flush=True)
            time.sleep(2)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/pingpong":
            counter = query("UPDATE counter SET value = value + 1 RETURNING value - 1")[0]
            body = f"pong {counter}"
        elif self.path == "/pings":
            body = str(query("SELECT value FROM counter")[0])
        else:
            self.send_error(404)
            return
        self.send_response(200)
        self.end_headers()
        self.wfile.write(body.encode())


signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

init_db()
print(f"Server started in port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()