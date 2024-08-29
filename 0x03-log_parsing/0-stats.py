#!/usr/bin/env python3
import sys

def print_stats(total_size, status_codes):
    """
    Print the accumulated metrics.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def main():
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) != 9:
                continue

            # Extract the file size and status code from the line
            try:
                file_size = int(parts[-1])
                status_code = int(parts[-2])
                total_size += file_size

                if status_code in status_codes:
                    status_codes[status_code] += 1
            except (ValueError, IndexError):
                continue

            line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    # Print final stats after all lines have been processed
    print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
