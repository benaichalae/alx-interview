#!/usr/bin/python3
'''A script for parsing HTTP request logs.
'''
import re
import sys


def extract_input(input_line):
    '''Extracts sections of a line of an HTTP request log.'''
    regex = (
        r'\s*(?P<ip>\S+)\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]\s*'
        r'"(?P<request>[^"]*)"\s*(?P<status_code>\S+)\s*(?P<file_size>\d+)'
    )
    match = re.match(regex, input_line)
    if match:
        status_code = match.group('status_code')
        file_size = int(match.group('file_size'))
        return status_code, file_size
    return None, 0


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.'''
    print(f'File size: {total_file_size}', flush=True)
    for status_code in sorted(status_codes_stats.keys()):
        num = status_codes_stats.get(status_code, 0)
        if num > 0:
            print(f'{status_code}: {num}', flush=True)


def update_metrics(line, total_file_size, status_codes_stats):
    '''Updates the metrics from a given HTTP request log.'''
    status_code, file_size = extract_input(line)
    if status_code in status_codes_stats.keys():
        status_codes_stats[status_code] += 1
    return total_file_size + file_size


def run():
    '''Starts the log parser.'''
    line_num = 0
    total_file_size = 0
    status_codes_stats = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0,
    }
    try:
        for line in sys.stdin:
            total_file_size = update_metrics(
                line,
                total_file_size,
                status_codes_stats,
            )
            line_num += 1
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
