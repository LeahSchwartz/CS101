'''
Created on Oct 12, 2017

@author: leahschwartz
'''
from math import sqrt
def isPrime(num):
    if num < 2:
        return False
    if num < 4:
        return True
    rangeNum = 3
    while True:
        if rangeNum > sqrt(num):
            primeAnswer = True
            break 
        if num % rangeNum == 0:
            primeAnswer = False
            break
        rangeNum = rangeNum  + 1
    return primeAnswer

def pcount(low,high):
    count = 0
    for num in range(low,high):
        if num % 2 != 0 or num == 2:
            if isPrime(num):
                print num
                count = count + 1 
    return count
if __name__ == '__main__':
    print pcount(1,15)