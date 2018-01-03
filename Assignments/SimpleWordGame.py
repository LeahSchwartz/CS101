'''
Created on Oct 29, 2017

@author: leahschwartz
'''
def points(player, dictionary):
    points = 0
    player = set(player)
    for word in player:
        if word in dictionary:
            points += len(word)**2
    return points
    
    
if __name__ == '__main__':
    print points(["apple", "orange", "strawberry" ], [ "strawberry", "orange", "grapefruit", "watermelon" ])