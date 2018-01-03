'''
Created on Sep 7, 2017

@author: leahschwartz
'''
def score(word):
    answer = len(word)**2
    return answer   
if __name__ == '__main__':
    print score("hi")