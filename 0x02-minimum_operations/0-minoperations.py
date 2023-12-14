#!/usr/bin/python3
'''The minimum operations coding challenge.
'''


def minOperations(n):
    '''Computes the fewest number of operations needed to result
    in exactly n H characters.

    Parameters:
    - n (int): The desired number of H characters.

    Returns:
    - int: The fewest number of operations needed.
    If n is impossible to achieve, returns 0.
    '''
    # Check if n is an integer
    if not isinstance(n, int):
        return 0

    # Initialize variables
    ops_count = 0        # Number of operations
    clipboard = 0        # Content in the clipboard
    done = 1             # Current content in the file

    while done < n:
        if clipboard == 0:
            # Initial copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            # Copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
        elif clipboard > 0:
            # Paste
            done += clipboard
            ops_count += 1

    return ops_count
