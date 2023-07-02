#!/usr/bin/python3
"""pascal's triangle"""

def pascal_triangle(n):
    """pascal triangle"""
    if n <= 0:
        return []
    
    outer = []

    for i in range(1, n+1):
        if i <= 2:
            inner = []
            for _ in range(i):
                inner.append(1)
            outer.append(inner)

        else:
            inner = []
            prev = outer[i-2]
            inner.append(1)
            for j in range(len(prev)-1):
                inner.append(prev[j] + prev[j+1])
            inner.append(1)
            outer.append(inner)
    return outer

