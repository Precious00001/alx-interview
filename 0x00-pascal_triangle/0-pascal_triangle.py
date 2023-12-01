#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''

def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    
    Args:
    n (int): The number of rows to generate in Pascal's triangle.

    Returns:
    list: A list of lists representing Pascal's triangle.
    '''

    triangle = []

    # Check if n is a positive integer
    if type(n) is not int or n <= 0:
        return triangle

    # Generate Pascal's triangle
    for i in range(n):
        line = []
        for j in range(i + 1):
            # Calculate values based on Pascal's triangle pattern
            if j == 0 or j == i:
                line.append(1)
            elif i > 0 and j > 0:
                line.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        triangle.append(line)

    return triangle
