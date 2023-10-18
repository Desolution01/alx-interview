#!/usr/bin/python3
"""
A script for parsing HTTP request logs.
"""
import re
import sys

def extract_input(input_line):
    """Extracts sections of a line of an HTTP request log."""
    fp = (
        r'\s*(?P<ip>\S+)\s*',
        r'\s*\[(?P<date>[^\]]+)\]',
        r'\s*"(?P<request>[^"]*)"',
        r'\s*(?P<status_code>\d+)',
        r'\s*(?P<file_size>\d+)'
    )
    log_fmt = '{}-{}-{}-{}-{}\\s*'.format(fp[0], fp[1], fp[2], fp[3], fp[4])
    resp_match = re.fullmatch(log_fmt, input_line)
    if resp_match:
        return (int(resp_match.group('status_code')), int(resp_match.group('file_size')))
    return None

def print_metrics(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count:
            print("{}: {}".format(code, count))

if __name__ == "__main__":
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    try:
        line_count = 0
        while True:
            line = sys.stdin.readline()
            line_count += 1
            if not line:
                break
            log_data = extract_input(line)
            if log_data:
                status_code, file_size = log_data
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1
            if line_count % 10 == 0:
                print_metrics(total_size, status_codes)
    except KeyboardInterrupt:
        pass
    print_metrics(total_size, status_codes)