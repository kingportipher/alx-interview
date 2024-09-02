#!/usr/bin/python3
"""
Log Parsing Script
"""

import sys
import re


def print_stats(log: dict) -> None:
    """
    Helper function to print statistics.
    """
    print("File size: {}".format(log["file_size"]))
    for code in sorted(log["code_frequency"]):
        if log["code_frequency"][code] > 0:
            print("{}: {}".format(code, log["code_frequency"][code]))


if __name__ == "__main__":
    # Regex to match the expected log format
    regex = re.compile(
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
    )

    line_count = 0
    log = {
        "file_size": 0,
        "code_frequency": {str(code): 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
    }

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                status_code = match.group(1)
                file_size = int(match.group(2))

                # Update total file size
                log["file_size"] += file_size

                # Update status code frequency
                if status_code in log["code_frequency"]:
                    log["code_frequency"][status_code] += 1

                # Print stats after every 10 lines
                if line_count % 10 == 0:
                    print_stats(log)

    except KeyboardInterrupt:
        print_stats(log)
        raise

    # Print final stats after reading all input lines
    print_stats(log)
