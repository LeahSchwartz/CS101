'''
Created on Dec 2, 2017

@author: leahschwartz
'''
def maximumFacts(suspects):
    commonList = []
    if len(suspects) == 1:
        return 0
    for index, person in enumerate(suspects):
        print index, person
        uniqueSuspect = suspects[index].split(","), index
        print uniqueSuspect
        otherSuspects = []
        for index, person in enumerate(suspects):
            person = person.split(","), index
            if person[1] != uniqueSuspect[1]:
                otherSuspects.append(person)
        print otherSuspects
        for person in otherSuspects:
            common = set(person[0]) & set(uniqueSuspect[0])
            commonList.append(len(common))
    return max(commonList)
        
    

    
     
if __name__ == '__main__':
    print maximumFacts(["medium,average,nondescript",
"medium,average,nondescript"])