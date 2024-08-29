#!/usr/bin/python3
import sys
import signal

def print_stats(total_size, status_counts):
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")

def signal_handler(sig, frame):
    print_stats(total_size, status_counts)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 7:
            continue

        ip, dash, date, request, http_version, status_code, file_size = parts
        
        try:
            file_size = int(file_size)
            status_code = int(status_code)
        except ValueError:
            continue

        if status_code in status_counts:
            status_counts[status_code] += 1
        
        total_size += file_size
        line_count += 1

        if line_count % 10 == 0:
            print_stats(total_size, status_counts)

except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    sys.exit(0)

