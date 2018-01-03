'''
Created on Sep 12, 2017

@author: leahschwartz
'''
def minutesNeeded (numCakes, capacity):
    if numCakes == 0:
        return 0
    if numCakes <= capacity:
        return 10
    if numCakes % capacity == 0:
        return numCakes / capacity * 10 
    #if remandier is half or less can do trick
    if numCakes % capacity <= capacity:
        if numCakes % capacity <= (capacity/2):
            return numCakes / capacity * 10 + 5
        else: 
            return numCakes / capacity * 10 + 10
    if numCakes % capacity >= capacity:
        return numCakes / capacity * 10
    return 10 
    
if __name__ == '__main__':
    pass

