#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    - data: List[int] - list of integers representing a UTF-8 encoded data set

    Returns:
    - bool: True if the data set is a valid UTF-8 encoding, False otherwise
    """
    nbytes = 0

    # Define bit masks for UTF-8 byte format
    v1 = 1 << 7
    v2 = 1 << 6

    for i in data:
        v = 1 << 7

        # Check the number of bytes needed to represent the current character
        if nbytes == 0:
            while v & i:
                nbytes += 1
                v = v >> 1

            if nbytes == 0:
                continue

            # Validate the number of bytes
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            # Check if the current byte is correctly formatted
            if not (i & v1 and not (i & v2)):
                return False

        # Decrease the number of remaining bytes for the current character
        nbytes -= 1

    # Check if all bytes are used (nbytes == 0) to represent valid UTF-8
    return nbytes == 0
