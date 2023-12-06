#!/usr/bin/python3
"""dhkl"""


import sys


def compute_metrics():
    """fjkk"""
    total_size = 0
    status_counts = {200: 0, 301: 0, 400: 0, 401: 0,
                       403: 0, 404: 0, 405: 0, 500: 0}
    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            ip, _, _, status_code, file_size = line.split()[0],
            line.split()[8], line.split()[10],
            line.split()[11], line.split()[12]
            total_size += int(file_size)
            if int(status_code) in status_counts:
                status_counts[int(status_code)] += 1
            if line_count % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)


def print_statistics(total_size, status_counts):
    """fjk"""
    print('Total file size:', total_size)
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(status_code, ':', status_counts[status_code])


compute_metrics()
