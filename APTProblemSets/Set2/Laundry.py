'''
Created on Sep 12, 2017

@author: leahschwartz
'''
def minutesNeeded(m):
    minutes = 60 + ((m-1) * 25)
    return minutes 
if __name__ == '__main__':
    print minutesNeeded(8)
