#!/usr/bin/python3
def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    result in exactly n H characters in the file.

    Parameters:
    - n (int): The desired number of H characters.

    Returns:
    - int: The fewest number of operations needed.
    If n is impossible to achieve, returns 0.
    """
    if n <= 1:
        return 0

    # Initialize the number of operations to 0
    operations = 0
    # Initialize the current buffer size to 1
    buffer_size = 1
    # Initialize the clipboard content to 0 (no content initially)
    clipboard_content = 0

    while buffer_size < n:
        if n % buffer_size == 0:
            # If the buffer size divides n, perform a Copy All operation
            clipboard_content = buffer_size
            # Increment the number of operations
            operations += 1

        # Perform a Paste operation, doubling the buffer size
        buffer_size += clipboard_content
        # Increment the number of operations
        operations += 1

    return operations
