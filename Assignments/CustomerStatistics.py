'''
Created on Nov 8, 2017

@author: leahschwartz
'''
def reportDuplicates(names):
    nameDict = {}
    for name in names:
        if name not in nameDict:
            nameDict[name] = 1
        else:
            nameDict[name] += 1
    nameList = [(key + " " + str(value)) for key,value in nameDict.items() if value > 1]
    return sorted(nameList)
if __name__ == '__main__':
    print reportDuplicates(["JOHN", "BOB", "JOHN", "BILL", "STANLEY", "JOHN"])