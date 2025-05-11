#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    fib_sequence = []
    if length >= 1:
        fib_sequence.append(0)
    
    if length >= 2:
        fib_sequence.append(1)
        
    a, b = 0, 1
    for _ in range(2, length):
        next_fib = a + b
        fib_sequence.append(next_fib)
        a, b = b, next_fib
        
    print(fib_sequence)
