'''
Created on Nov 6, 2017

@author: leahschwartz
'''
def computeNames(team1, count, team2):
    firstNameSet1 = set()
    firstNameSet2 = set()
    for number in range(0,len(team1.split()), 2):
        firstNameSet1.add(team1.split()[number])
    for number in range(0, len(team2.split()), 2):
        firstNameSet2.add(team2.split()[number])
    uniqueNames = firstNameSet1 ^ firstNameSet2
    return " ".join(sorted(list(uniqueNames)))

    
    
    
if __name__ == '__main__':
    print computeNames("Joe Smith Wes Smith Joe Wright Craig Wills", 2, "Bill Carter Wes Mitchell Craig Smith")