#!/usr/bin/env python3

#what is happening below is that we are defining a function to generate a Fibonacci sequence
#the function takes a single argument 'length' which determines how many numbers in the sequence to generate
#the function returns a list containing the Fibonacci sequence up to the specified length
## the Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones
## the function handles edge cases for lengths less than or equal to 0, and for lengths of 1 or 2

def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    elif length == 1:   ## if the length is 1, return a list with only the first Fibonacci number
        print([0])
        return
    elif length == 2:    ## if the length is 2, return a list with the first two Fibonacci numbers
        print([0, 1])
        return

    fib_sequence = [0, 1]     # initialize the sequence with the first two Fibonacci numbers
    # generate the Fibonacci sequence up to the specified length
     # starting from the third number (index 2)
    for i in range(2, length):
        # i is the current index in the sequence
        # fib_sequence[i - 1] is the last number in the sequence
        # fib_sequence[i - 2] is the second last number in the sequence
        next_value = fib_sequence[i - 1] + fib_sequence[i - 2]        # calculate the next Fibonacci number
        fib_sequence.append(next_value)    # append the next number to the sequence

    print(fib_sequence)