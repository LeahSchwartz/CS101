'''
Created on Dec 4, 2017

@author: leahschwartz
'''
def winners(data):
    winDict = {}
    for item in data:
        person = item.split()[0]
        time = item.split()[1]
        mins = time.split(":")[0]
        secs = time.split(":")[1]
        totalTime = (int(mins) * 60 + float(secs)) / 60
        if person not in winDict:
            winDict[person] = [(totalTime, 1)]
        else:
            winDict[person] = [(tuple[0] + totalTime, tuple[1] + 1) for tuple in winDict[person]]
    tupleList = winDict.items()
    print tupleList
    sortedInfo = sorted(tupleList, key = lambda x:(-x[1][0][1], x[1][0][0]))
    returnInfo = [t[0] for t in sortedInfo]
    return returnInfo
    
    
if __name__ == '__main__':
    print winners(["owen 2:00", "jeff 1:29", "owen 1:00", "jeff 1:30", "robert 0:21"])
