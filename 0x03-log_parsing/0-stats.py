#!/usr/bin/python3
import sys

def print_stats(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            parts = line.split()
            
            # Skip lines with incorrect format
            if len(parts) != 12 or parts[8] != '"GET' or parts[10] != 'HTTP/1.1"':
                continue
            
            # Parse file size and status code
            file_size = int(parts[11])
            status_code = int(parts[9])

            # Update total file size
            total_size += file_size

            # Update status counts
            if status_code in status_counts:
                status_counts[status_code] += 1
            else:
                status_counts[status_code] = 1

            # Print stats every 10 lines
            if i % 10 == 0:
                print_stats(total_size, status_counts)
    
    except KeyboardInterrupt:
        # Handle keyboard interruption and print final stats
        print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()

