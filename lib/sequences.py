#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence=[0,1]

    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    
    
    while len(fibonacci_sequence)<length:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)

    print(fibonacci_sequence[:length])
       
    pass