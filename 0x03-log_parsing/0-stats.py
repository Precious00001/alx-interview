#!/usr/bin/python3
"""Script that reads stdin line by line and computes metrics."""

import sys

# Initialize variables
i = 0
sum_file_size = 0
status_code = {'200': 0,
               '301': 0,
               '400': 0,
               '401': 0,
               '403': 0,
               '404': 0,
               '405': 0,
               '500': 0}

try:
    # Read input lines from stdin
    for line in sys.stdin:
        # Split the line into individual words
        args = line.split(' ')

        # Check if the line has enough words
        if len(args) > 2:
            # Extract status line and file size
            status_line = args[-2]
            file_size = args[-1]

            # Update status code counts
            if status_line in status_code:
                status_code[status_line] += 1

            # Update total file size
            sum_file_size += int(file_size)
            i += 1

            # Print metrics every 10 lines
            if i == 10:
                print('File size: {:d}'.format(sum_file_size))
                sorted_keys = sorted(status_code.keys())
                for key in sorted_keys:
                    value = status_code[key]
                    if value != 0:
                        print('{}: {}'.format(key, value))
                i = 0

except Exception:
    pass
finally:
    # Print final metrics
    print('File size: {:d}'.format(sum_file_size))
    sorted_keys = sorted(status_code.keys())
    for key in sorted_keys:
        value = status_code[key]
        if value != 0:
            print('{}: {}'.format(key, value))
