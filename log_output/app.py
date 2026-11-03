import signal
import sys
import time
import uuid
from datetime import datetime, timezone

RANDOM_STRING = str(uuid.uuid4())

def timestamp():
    return datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")


signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

while True:
    print(f"{timestamp()}: {RANDOM_STRING}", flush=True)
    time.sleep(5)