'''
Created on Sep 24, 2017

@author: leahschwartz
'''
def computeCups(calplan, eaten, calperserv, servsize):
    if eaten >= calplan:
        fullCups = 0
    else:
        caloriesLeft = calplan - eaten
        servingstoHave = caloriesLeft / float(calperserv)
        fullCups = servingstoHave * servsize 
        fullCups = int(fullCups)
    return fullCups
     
    
    
if __name__ == '__main__':
    print computeCups(2400, 1275, 60, .5)