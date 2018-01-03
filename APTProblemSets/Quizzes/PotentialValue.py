'''
Created on Sep 24, 2017

@author: leahschwartz
'''
def compute(itema, itemb):
    answer = (5* float(itema) / 3) + ((float(itemb)**2)/7 )
    return answer

if __name__ == '__main__':
    print compute(9, 3)