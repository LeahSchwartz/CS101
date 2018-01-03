'''
Created on Nov 8, 2017

@author: leahschwartz
'''
def whosDishonest(club1, club2, club3):
    cheatersSet = set()
    club1Set = set(club1)
    club2Set = set(club2)
    club3Set = set(club3)
    bigSet = club1Set | club2Set | club3Set
    for name in bigSet:
        if name in club1Set & club2Set or name in club1Set & club3Set or name in club2Set & club3Set:
            cheatersSet.add(name) 
    return sorted(list(cheatersSet))
    
    
    
if __name__ == '__main__':
    print whosDishonest(["JOHN","JOHN","FRED","PEG"], ["PEG","GEORGE"], ["GEORGE","DAVID"])