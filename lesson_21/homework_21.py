import logging
from datetime import datetime

KEY = "Key TSTFEED0300|7E3E|0400"
LOG_FILE = "hblog.txt"
OUTPUT_FILE = "hb_test.log"

logging.basicConfig(
    filename=OUTPUT_FILE,
    filemode="w",
    level=logging.INFO,
    format="%(levelname)s at %(message)s",
    datefmt="%H:%M:%S"
)

def get_timestamp(line):
    try:
        return datetime.strptime(line.split("Timestamp ")[1][:8], "%H:%M:%S")
    except (IndexError, ValueError):
        return None

def verify_heartbeat(log_path, key):
    with open(log_path, "r") as f:
        filtered_log = [line.strip() for line in f if key in line]

    for i in range(1, len(filtered_log)):
        prev_ts = get_timestamp(filtered_log[i - 1])
        curr_ts = get_timestamp(filtered_log[i])
        if prev_ts and curr_ts:
            delta = abs((curr_ts - prev_ts).total_seconds())
            if 31 < delta < 33:
                logging.warning(f"{curr_ts.strftime('%H:%M:%S')} - heartbeat = {delta} seconds")
                logging.warning(f"line - {filtered_log[i]}")
            elif delta >= 33:
                logging.error(f"{curr_ts.strftime('%H:%M:%S')} - heartbeat = {delta} seconds")
                logging.error(f"line - {filtered_log[i]}")

verify_heartbeat(LOG_FILE, KEY)