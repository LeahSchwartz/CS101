'''
Created on Sep 7, 2017

@author: leahschwartz
'''
def convert(red,green,blue):
    answer = (0.21*red) + (0.71*green) + (0.07*blue)
    return answer
if __name__ == '__main__':
    print convert(255,255,255)
