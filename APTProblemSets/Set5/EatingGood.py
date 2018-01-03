'''
Created on Oct 24, 2017

@author: leahschwartz
'''
def howMany(meals, restaurant):
    answerList = []
    for item in meals:
        itemSplit = item.split(":")
        if itemSplit[1] == restaurant and itemSplit[0] not in answerList:
            answerList.append(itemSplit[0])
    return len(answerList)
        
if __name__ == '__main__':
    print howMany(["Sue:Elmos", "Sue:Elmos", "Sue:Elmos"], "Elmos")