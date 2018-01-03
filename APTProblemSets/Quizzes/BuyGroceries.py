'''
Created on Nov 6, 2017

@author: leahschwartz
'''

def pickBest(groceries):
    priceDict = {}
    payList = []
    groceries = groceries.split(",")
    for item in groceries:
        food = item.split(":")[0]
        price = (item.split(":")[1])
        if food not in priceDict:
            priceDict[food] = [float(price)]
        else:
            priceDict[food] += [float(price)]
    print priceDict
    for key, value in priceDict.items():
        print sorted(value)
        payList += [(sorted(value)[0])]
    return sum(payList)
        
    
if __name__ == '__main__':
    print pickBest("peas:9.0,lotion:11.50,lotion:6.5,peas:3.5,lotion:6.2,peas:3.5,peas:3.1,lotion:6.7")