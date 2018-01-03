'''
Created on Oct 31, 2017

@author: leahschwartz
'''
def networth(transactions):
    transDict = {}
    transAnswerList = []
    for element in transactions:
        fromP = element.split(":")[0]
        toP = element.split(":")[1]
        amount = float(element.split(":")[2])
        if fromP not in transDict:
            transDict[fromP] = 0 - amount
        else:
            transDict[fromP] += -amount
        if toP not in transDict:
            transDict[toP] = amount
        else: 
            transDict[toP] += amount
    for item, value in transDict.items():
        transDict[item] = (round(value, 2))
        transAnswerList.append("".join([item,":",str(value)]))
    return sorted(transAnswerList)
if __name__ == '__main__': 
    print networth(["fred:ricky:50", "ricky:fred:20", "fred:ethel:100", "ethel:fred:150.35"])