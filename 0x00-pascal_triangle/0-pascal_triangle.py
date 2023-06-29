#!/usr/bin/python3
"""
Function that returns the pascal triangle
Assumes that n is always an integer
"""
def pascal_triangle(n):
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1],[1,1]]
    else:
        lis = [1]
        triangle = pascal_triangle(n - 1)
        tri = triangle[-1]
        for i in range(len(tri) - 1):
            var = tri[i] + tri[i+1]
            lis.append(var)
        lis.append(1)
        triangle.append(lis)
        return triangle
