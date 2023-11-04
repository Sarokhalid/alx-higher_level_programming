#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a[:2]
    b = tuple_b[:2]
    a += (0,) * (2 - len(a))
    b += (] + b[0], a[1] + b[1])
    result = (a[0] + b[0], a[1] + b[2])
    return result
