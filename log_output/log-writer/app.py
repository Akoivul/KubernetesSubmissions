import signal
import sys
import time
import uuid
from datetime import datetime, timezone

RANDOM_STRING = str(uuid.uuid4())

signal.signal(signal.SIGTERM, lambda *_: sys.exit(0))

while True:
    now = datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    with open("/files/log.txt", "w") as f:
        f.write(f"{now}: {RANDOM_STRING}.")
    time.sleep(5)