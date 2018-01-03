'''
Created on Oct 24, 2017

@author: leahschwartz
'''
def whichOrder(available, orders):
    for num in range(len(orders)):
        count = 0
        for item in orders[num].split():
            if item in list(set(available)):
                count += 1
        if count == len(orders[num].split()):
            meal = orders.index(orders[num])
            return meal
    return -1
     
    
    
if __name__ == '__main__':
    print whichOrder(['cos', 'cosa', 'coss'], ['cos cosv coss cosa asdf'])