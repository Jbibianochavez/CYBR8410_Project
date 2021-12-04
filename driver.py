#!/usr/bin/env python3

import hashlib

def main():
    NUM_ZEROS = 4
    Serial = "123456789"
    MAC = "AD:CD:EF:12:34:56:78:90"
    
    NUM_ZEROS = getUserInput()
    netHash = calcNetworkHash(Serial, MAC)
    nonce, hashVal = mineNetworkKey(netHash, NUM_ZEROS)
    minedPassword = nonce
    print("Nonce: " + str(minedPassword))
    print("HashVal: " + hashVal.hexdigest())
    
def getUserInput():
    userInput = int(input("How Many Leading Zeros? "))
    return userInput
    
def calcNetworkHash(Serial, MAC):
    concat = Serial + MAC
    netHash = getHash(concat)
    #print(netHash.hexdigest())
    return netHash
    
def mineNetworkKey(netHash, numZeros):
    nonce = 0;
    concat = netHash.hexdigest() + str(nonce)
    hashVal = getHash(concat)
    valid = checkValid(numZeros, hashVal.hexdigest())
    #print("Valid = " + str(valid))
    #print(type(valid))
    
    while(valid == 0):
        #print("Here")
        nonce = nonce + 1
        concat = netHash.hexdigest() + str(nonce)
        hashVal = getHash(concat)
        #print(hashVal.hexdigest())
        valid = checkValid(numZeros, hashVal.hexdigest())
        #print("Is valid? " + str(valid))
        
    return nonce, hashVal
    
def getHash(inputVal):
    hasher = hashlib.sha256()
    valHash = hashlib.sha256((inputVal).encode())
    #print(netHash.hexdigest())
    return valHash
    
def checkValid(numZeros, inputCheck):
    notZero = 1
    
    for x in range(numZeros):
        #print(inputCheck[x])
        if (inputCheck[x] != '0'):
            #print("Not Zero")
            notZero = 0

    return notZero

if __name__ == "__main__":
    main()
