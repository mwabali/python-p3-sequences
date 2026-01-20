#!/usr/bin/env python3

def print_fibonacci(length):
    pass
    if length <= 0:
        print("[]")
        return


    fib=[0,1]
    while len(fib) < length:
        next_num = fib[-1] + fib[-2]
        fib.append(next_num)
        

    print(fib[:length])