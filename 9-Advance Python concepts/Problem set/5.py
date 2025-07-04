#5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [111, 2, 65, 54, 34, 43, 645, 75, 45, 55]

def greater(a, b):
    if(a>b):
        return a 
    return b 

print(reduce(greater, l))