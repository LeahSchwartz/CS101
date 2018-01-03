'''
Created on Dec 2, 2017

@author: leahschwartz
'''
import operator

def generate(results):
    medalDict = {}
    for item in results:
        countryList = item.split()
        for num in range(len(countryList)):
            country = countryList[num]
            if countryList[num] not in medalDict:
                medalDict[country] = [0,0,0]
            if num == 0:
                medalDict[country][0] += 1
            if num == 1:
                medalDict[country][1] += 1   
            if num == 2:
                medalDict[country][2] += 1
        tupleList = medalDict.items()
    aInfo = sorted(tupleList, key=operator.itemgetter(0))
    print aInfo
    sortedInfo = sorted(aInfo, key=operator.itemgetter(1), reverse = True)
    print sortedInfo
    #sortedInfo = sorted(tupleList, key = lambda x: (-x[1][0], -x[1][1], -x[1][2], x[0]))
    returnInfo = [(t[0] + " " + str(t[1][0]) + " " + str(t[1][1]) + " " + str(t[1][2])) for t in sortedInfo]
    return returnInfo
    
if __name__ == '__main__':
    print generate(["ITA JPN AUS", "KOR TPE UKR", "KOR KOR GBR", "KOR CHN TPE"])