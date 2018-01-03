'''
Created on Nov 7, 2017

@author: leahschwartz
'''
def freqs(data):
    fruitDict = {}
    freqList = []
    for fruit in data:
        if fruit not in fruitDict:
            fruitDict[fruit] = 1
        else:
            fruitDict[fruit] += 1
    sortedFruit = sorted(fruitDict.items())
    for element in sortedFruit:
        freqList.append(element[1])
    return freqList

if __name__ == '__main__':
    print freqs(["apple", "cherry", "pear","apple", "cherry", "pear", "apple", "banana"])