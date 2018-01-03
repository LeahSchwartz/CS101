'''
Created on Oct 13, 2017

@author: leahschwartz
'''
def getMinimum(s, oCost, xCost):
    pos = 0
    answer = 0
    sList = list(s) 
    while True:
        if pos >= len(sList):
            break
        if sList[pos] == "?":
            if sList[-pos - 1] == "x":
                sList[pos] = "x"
                answer += xCost 
            if sList[-pos - 1] == "o":
                sList[pos] = "o"  
                answer += oCost
            if sList[-pos - 1] == "?":
                if oCost < xCost:
                    sList[pos] = "o"
                    answer += oCost
                else:
                    sList[pos] = "x"
                    answer += xCost
        pos += 1
    if sList[::-1] != sList and "?" not in sList:
        answer = -1     
    return answer
    
if __name__ == '__main__':
    print getMinimum("oxo?xox?", 9, 4)