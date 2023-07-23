#!/usr/bin/env python3
fibonacci_list = []

def print_fibonacci(length):
    if length == 0:     
       fibonacci_list = []
       return print(fibonacci_list)
    elif length  == 1:
       fibonacci_list = [0]
       return print(fibonacci_list)
    elif length  == 2:
       fibonacci_list = [0, 1]
       return print(fibonacci_list)
    else:
        fibonacci_list = [0, 1]
        for i in range(2, length):
            next_number = fibonacci_list[-1] + fibonacci_list[-2]
            fibonacci_list.append(next_number)
        return print(fibonacci_list)