'''
Created on Nov 7, 2017

@author: leahschwartz
'''
def nameDonor(contributions):
    donorDict = {}
    biggestDonor = ""
    biggestDonation = 0
    for line in contributions:
        person = line.split(":")[0]
        amount = float(line.split(":")[1])
        if person not in donorDict:
            donorDict[person] = amount
        else:
            donorDict[person] += amount
    for key,value in donorDict.items():
        if value > biggestDonation or (value == biggestDonation and key < biggestDonor):
            biggestDonation = value
            biggestDonor = key
    return biggestDonor
        


if __name__ == '__main__':
    print nameDonor(['Sun:70.00', 'Zebra:80.00', 'Blue:80.00', 'Edwards:50.00'])