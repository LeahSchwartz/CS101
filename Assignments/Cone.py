'''
Created on Sep 7, 2017

@author: leahschwartz
'''
import math
def volume(radius,height):
    answer = 1.0/3.0 * math.pi * radius**2 * height
    return answer
    

if __name__ == '__main__':
    print volume(2.0,3.0)