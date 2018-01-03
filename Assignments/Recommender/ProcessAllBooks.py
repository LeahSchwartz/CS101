'''
Created on Nov 28, 2017

@author: leahschwartz
'''
def readFile(filename):
    #opens file and returns it as a list of lines
    f = open(filename)
    r = f.read()
    f.close()
    return r.split("\n")

def buildDict(bList, bookratings):
    #builds rater dictionary
    bDict = {}
    rater = ""
    itemList = []
    for line in bookratings: #puts each item in doc into list
        item = line.split(":")
        itemList.extend(item)
    for num in range(len(itemList)): #sets rater to person's name
        if itemList[num] == "RATER":
            rater = itemList[num + 1] #next item is person
            bDict[rater] = []
        elif itemList[num].isdigit() or itemList[num].startswith("-"): #rating or neg rating
            item = int(itemList[num]) #makes int
            bDict[rater] += [item] #adds to dict
    return bDict 
        
def bookList(booktitle):
    #creates list of titles and authors
    bList = [] 
    for num in range(0,len(booktitle) - 1, 2): #goes over every other (title)
        book = booktitle[num].split(".")[1]
        author = booktitle[num + 1].split(".")[1]
        item = book+","+author
        bList.append(item) #adds as one item to list
    return bList
    
def processdata(booktitle, bookratings):
    #calls two functs to create list and dictionary
    booktitle = readFile(booktitle)
    bookratings = readFile(bookratings)
    itemlist = bookList(booktitle)
    raterdict = buildDict(itemlist, bookratings)
    return itemlist, raterdict

if __name__ == '__main__':
    booktitle = "AllBooksAuthors.txt"
    bookratings = "AllBooksRatings.txt"
    print processdata(booktitle, bookratings)