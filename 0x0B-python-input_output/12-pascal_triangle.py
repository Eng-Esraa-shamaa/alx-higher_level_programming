#!/usr/bin/python3
"""
Technical interview preparation
"""


def pascal_triangle(n):
    """
    Args:
        n: representation of pascal triangle
    """
    if n <= 0:
        return []
    triangle = []
    start = [0, 1, 0]
    for i in range(n):
        triangle.append(start[1:-1])
        new_triangle = [start[i] + start[i + 1] for i in range(len(start) - 1)]
        start = [0] + new_triangle + [0]
    return triangle
