#!/usr/bin/env python3
import sys
import signal
import re

# Initialize metrics
total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

# Regular expression to match the log format
log_pattern = re.compile(r'^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')

def print_stats():
    """
    Print the accumulated metrics.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def signal_handler(sig, frame):
    """
    Handle the keyboard interruption signal (CTRL + C).
    """
    print_stats()
    sys.exit(0)

# Set up signal handling for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = log_pattern.match(line.strip())
        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))

            # Update the metrics
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            # Print the metrics every 10 lines
            if line_count % 10 == 0:
                print_stats()

except Exception as e:
    print(f"An error occurred: {e}", file=sys.stderr)

# Print final stats when the input ends
print_stats()

