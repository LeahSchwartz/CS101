'''
Created on Nov 27, 2017

@author: leahschwartz
'''
def readFile(filename):
    #opens file and returns it as a list of lines
    f = open(filename)
    r = f.read()
    f.close()
    return r.split("\n")

def restaurantList(filename):
    #returns a list of unique restaurants represented by the data
    restSet = set()
    for line in filename:
        if line.startswith("("):
            line = line[1:-1]
            rest = line.split(")")[0]
            restSet.add(rest)
    return sorted(list(restSet))
    
def processdata(filename):
    #returns list of restaurants and dict of ordered ratings
    eatDict = {}
    r = readFile(filename)
    rList = restaurantList(r) #unique rest list
    name = ""
    for line in r: #builds dict based on rated rests
        if not line.startswith("("): #sees if line is name
            name = line
        else: #otherwise line is rest and rating
            rest = line.split(")")[0][1:] 
            rate = int(line.split(")")[1][1:])
            if name not in eatDict: #value is list of tuples
                eatDict[name] = [(rest, rate)]
            else:
                eatDict[name] += [(rest, rate)]
    for key, value in eatDict.items(): #adds in 0 rating for unrated rests
        restSet = set()  
        rSet = set(rList)
        for rest in value:
            restSet.add(rest[0])
        unincluded = rSet - restSet #rests that have not been rated  
        for item in unincluded:
            eatDict[key] += [(item, 0)]       
        eatDict[key] = sorted(value) #sorts for same order
    for key, value in eatDict.items():
        ratingList = []
        tupleList = value
        for item in tupleList:
            ratingList.append(item[1])
        eatDict[key] = ratingList
    itemList = rList
    dictratings = eatDict
    return itemList, dictratings
         
if __name__ == '__main__':
    filename = "AllFoodRatings.txt"
    #print readFile(filename)
    print processdata(filename)