'''
Created on Dec 2, 2017

@author: leahschwartz
'''
import operator  

def sort(data):
    fruitDict = {}
    for item in data:
        if item not in fruitDict:
            fruitDict[item] = 1
        else:
            fruitDict[item] += 1
    tupleList = fruitDict.items()
    #sortedList = sorted(tupleList, key=lambda x: (-x[1], x[0]))
    aList = sorted(tupleList, key=operator.itemgetter(0))
    print aList
    sortedList = sorted(aList, key=operator.itemgetter(1), reverse = True)
    print sortedList
    returnInfo = [t[0] for t in sortedList]
    return returnInfo        
       
if __name__ == '__main__':
    print sort(['cherry', 'cherry', 'cherry', 'apple', 'apple', 'apple', 'banana', 'banana', 'asparagus', 'asparagus', 'watermelon', 'orange'])
    
    