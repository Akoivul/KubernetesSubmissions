import signal
import sys
import time
import uuid
from datetime import datetime, timezone

RANDOM_STRING = str(uuid.uuid4())

signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

while True:
    with open("/files/log.txt", "a") as f:
        f.write(f"{datetime.now(timezone.utc).isoformat()}: {RANDOM_STRING}\n")
    time.sleep(5)