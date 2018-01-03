'''
Created on Dec 3, 2017

@author: Leah
'''
    
def getNums(alist):  
    answer = [] 
    for item in alist:
        if type(item) == int:
            answer.append(item)
        else:
            answer += getNums(item)
    return answer
    
if __name__ == '__main__':
    alist = [3, [4,7]]
    blist = getNums(alist)
    print "alist is", alist
    print "The list returned from getNums is"
    print blist
    print
    
    alist = [[4,[7]], 3]
    blist = getNums(alist)
    print "alist is", alist
    print "The list returned from getNums is"
    print blist
    print

    alist = [5, [6,7], 8, [ [1], [2, [6]], 7]]
    blist = getNums(alist)
    print "alist is", alist
    print "The list returned from getNums is"
    print blist
    print
    alist = [5, 2, [6, [8,1], 7], 8, [ [1], [[4, [5]], 2, [6]], 7]]
    blist = getNums(alist)
    print "alist is", alist
    print "The list returned from getNums is"
    print blist   