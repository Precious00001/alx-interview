#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

# Generate 10,000 log entries
for i in range(10000):
    # Introduce a random delay to simulate a real log generator
    sleep(random.random())

    # Create a log entry with a random IP address, timestamp, HTTP status code, and file size
    log_entry = "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    )

    # Write the log entry to the standard output (sys.stdout)
    sys.stdout.write(log_entry)

    # Flush the output to ensure immediate display
    sys.stdout.flush()
