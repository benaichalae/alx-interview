#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import sys
from collections import defaultdict


def print_statistics(file_size, status_counts) -> None:
    """Prints file size and status code"""
    print(f"File size: {file_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


if __name__ == '__main__':
    total_file_size = 0
    status_code_counts = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.strip().split()

            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])

                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1

                total_file_size += file_size

                if line_count % 10 == 0:
                    print_statistics(total_file_size, status_code_counts)

            except (ValueError, IndexError):
                continue

        print_statistics(total_file_size, status_code_counts)

    except KeyboardInterrupt:
        print_statistics(total_file_size, status_code_counts)
        raise
