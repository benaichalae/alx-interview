#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys
from collections import defaultdict


def print_statistics(total_file_size, status_code_counts):
    print(f"File size: {total_file_size}")
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")


def process_line(line):
    parts = line.split()
    if len(parts) != 10:
        return None, None
    try:
        status_code = int(parts[-2])
        file_size = int(parts[-1])
        return status_code, file_size
    except ValueError:
        return None, None

    if __name__ == "__main__":
        total_file_size = 0
        status_code_counts = defaultdict(int)
        line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = process_line(line.strip())
            if status_code is None:
                continue

            status_code_counts[status_code] += 1
            total_file_size += file_size

            if line_count % 10 == 0:
                print_statistics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)
        sys.exit(0)

    print_statistics(total_file_size, status_code_counts)
