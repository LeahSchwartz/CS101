'''
Created on Sept 24, 2017

@author: leahschwartz
'''


def process(name):
    # name is a file, returns a list of strings 
    #    from the file
    f = open(name)
    answer = []
    for line in f:
        line = line.strip()
        line = line.split(":")
        answer.append(line)
    return answer

def averageHeight(personList):
    heights = [] 
    totalHeights = 0
    for item in personList:
        heights.append(float(item[4]))
    totalHeights = sum(heights) / len(personList)
    return totalHeights
        
def heightRange(personList, height1, height2):
    goodHeights = [] 
    for line in personList:
        if float(line[4]) >= height1 and float(line[4]) <= height2:
            goodHeights.append(line)
    return goodHeights

def group(data, gender, sport):
    goodPersonList = []
    for line in data:
        if line[2] == gender and line[3]== sport:
            goodPersonList.append(line)
    return goodPersonList
        


if __name__ == '__main__':
    filename = "athletes.txt"
    data = process(filename)
    print "THE DATA IS:"
    for item in data:
        print item
    print
    print averageHeight(data)
    print heightRange(data,72,78 )
    print heightRange(data, 74, 74)
    print len(heightRange(data, 72, 78))
    print group(data, "women", "tennis")
    print len(group(data, "women", "tennis"))
    print averageHeight(group(data, "women", "tennis"))
    womensbb = averageHeight(group(data, "women", "basketball"))
    mensbb = averageHeight(group(data, "men", "basketball"))
    print (womensbb + mensbb) / 2