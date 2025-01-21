#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure each tuple has at least 2 elements, padding with 0 if necessary
    a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    b = tuple_b + (0, 0)[:2 - len(tuple_b)]
    
    # Add the first two elements of each tuple
    return (a[0] + b[0], a[1] + b[1])
