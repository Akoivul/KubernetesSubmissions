import json
import os
import signal
import sys
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

import psycopg

PORT = int(os.environ["PORT"])


def query(sql, params=()):
    with psycopg.connect(autocommit=True) as conn:
        cur = conn.execute(sql, params)
        return cur.fetchall() if cur.description else None


def init_db():
    while True:
        try:
            query("CREATE TABLE IF NOT EXISTS todos (id SERIAL PRIMARY KEY, content TEXT NOT NULL)")
            return
        except psycopg.OperationalError as e:
            print(f"Waiting for database: {e}", flush=True)
            time.sleep(2)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/todos":
            self.send_error(404)
            return
        todos = [row[0] for row in query("SELECT content FROM todos ORDER BY id")]
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
        if not todo or len(todo) > 140:
            print(f"Rejected todo ({len(todo)} characters): {todo}", flush=True)
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Todo must be 1-140 characters\n")
            return
        query("INSERT INTO todos (content) VALUES (%s)", (todo,))
        print(f"Added todo: {todo}", flush=True)
        self.send_response(303)
        self.send_header("Location", "/")
        self.end_headers()


signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

init_db()
print(f"Server started in port {PORT}", flush=True)
HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()