#!/usr/bin/python3
import sys

def print_stats(status_counts, total_size):
    print("File size: {}".format(total_size))
    sorted_codes = sorted(status_counts.keys())
    for code in sorted_codes:
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_size = 0
line_count = 0

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) >= 9:
            status = int(parts[-2])
            if status in status_counts:
                status_counts[status] += 1
            total_size += int(parts[-1])
            line_count += 1
            if line_count % 10 == 0:
                print_stats(status_counts, total_size)

except KeyboardInterrupt:
    pass

print_stats(status_counts, total_size)
