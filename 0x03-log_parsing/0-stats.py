#!/usr/bin/python3

import sys

# Initialize dictionaries to store status codes and file sizes
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

total_file_size = 0
line_count = 0

def print_metrics():
    """Print metrics including file size and status code counts."""
    print("Total file size: {}".format(total_file_size))
    for status in sorted(status_codes.keys()):
        if status_codes[status]:
            print("{}: {}".format(status, status_codes[status]))

try:
    for line in sys.stdin:
        try:
            # Split the line into elements
            elems = line.split()
            
            # Ensure the line matches the expected format
            if len(elems) >= 7:
                file_size = int(elems[-1])
                status_code = elems[-2]
                
                # Update the total file size
                total_file_size += file_size
                
                # Update status code counts
                if status_code in status_codes:
                    status_codes[status_code] += 1
        except ValueError:
            pass

        # Update line count
        line_count += 1

        # Check if we should print metrics
        if line_count % 10 == 0:
            print_metrics()

except KeyboardInterrupt:
    # Handle Ctrl+C by printing metrics
    print_metrics()
    raise

# Print final metrics
print_metrics()
