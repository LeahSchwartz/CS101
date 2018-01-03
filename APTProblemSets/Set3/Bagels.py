'''
Created on Sep 20, 2017

@author: leahschwartz
'''
def bagelCount(orders):
    bagelsNeeded = 0
    bagelsNeededList = []
    bagelsTotal = 0
    for number in orders:
        bagelsNeededList.append(number)
        if number >= 12:
            bagelsNeeded = number / 12
            bagelsNeededList.append(bagelsNeeded)
    bagelsTotal = sum(bagelsNeededList)
    return bagelsTotal        
        
if __name__ == '__main__':
    print bagelCount([14, 12])
