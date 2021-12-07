#!/usr/bin/env python3

import hashlib
import random

def main():
    NUM_ZEROS = 4
    Serial = "123456789"
    MAC = "AD:CD:EF:12:34:56:78:90"
    
    print("*****CALCULATE PASSWORD*****")
    NUM_ZEROS = getUserInput()
    netHash = calcNetworkHash(Serial, MAC)
    nonce, hashVal = mineNetworkKey(netHash, NUM_ZEROS)
    minedPassword = nonce
    print("Password: " + str(minedPassword))
    print("HashVal: " + hashVal.hexdigest())
    
    return minedPassword, netHash, hashVal
    
def getUserInput():
    userInput = int(input("How Many Leading Zeros? "))
    return userInput
    
def calcNetworkHash(Serial, MAC):
    concat = Serial + MAC
    netHash = getHash(concat)
    return netHash
    
def mineNetworkKey(netHash, numZeros):
    nonce = random.randint(1000000000000, 100000000000000000);
    concat = netHash.hexdigest() + str(nonce)
    hashVal = getHash(concat)
    valid = checkValid(numZeros, hashVal.hexdigest())
    
    #needs randomized
    while(valid == 0):
        nonce = nonce + 1
        concat = netHash.hexdigest() + str(nonce)
        hashVal = getHash(concat)
        valid = checkValid(numZeros, hashVal.hexdigest())
        
    return nonce, hashVal
    
def getHash(inputVal):
    hasher = hashlib.sha256()
    valHash = hashlib.sha256((inputVal).encode())
    return valHash
    
def checkValid(numZeros, inputCheck):
    notZero = 1
    
    for x in range(numZeros):
        if (inputCheck[x] != '0'):
            notZero = 0

    return notZero

if __name__ == "__main__":
    main()
