import logging, os
from logging.handlers import RotatingFileHandler
from datetime import datetime

EVENT_LOG = os.path.join(os.path.dirname(__file__), "..", "events.log")
logger = logging.getLogger("QVWAP")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler(EVENT_LOG, maxBytes=5*1024*1024, backupCount=3)
handler.setFormatter(logging.Formatter('%(message)s'))
logger.addHandler(handler)

def emit_event(event_type, message): 
    ts = datetime.now().strftime('%H:%M:%S')
    msg = f"{event_type}|{ts}|{message}"
    print(f"[{ts}] {msg}")
    logger.info(msg)
