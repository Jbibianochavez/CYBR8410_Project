#!/usr/bin/env python3

import minePassword
from datetime import datetime

def main(networkHash, authHash):
    clientSerial = "958674152"
    clientMAC = "AA:BB:CC:DD:EE:55:66:99"
    #minedPassword, networkHash, authHash = minePassword.main()
    authentication = authenticate(networkHash, authHash)
    loginBlock = genLoginBlock(authentication, clientMAC, authHash)
    success = checkLoginBlock(loginBlock)
    if(success == 1):
        return loginBlock
    else:
        return 0
    
def authenticate(networkHash, authHash):
    print("\n*****BEGIN AUTHENTICATION*****")
    userPass = getUserInput()
    valid = checkPassword(userPass, networkHash, authHash)
    return valid
    
def getUserInput():
    userPass = int(input("Please enter the password: "))
    return userPass
    
def checkPassword(userPass, networkHash, authHash):
    valid = 0
    concat = networkHash.hexdigest() + str(userPass)
    attemptHash = minePassword.getHash(concat)
    if(attemptHash.hexdigest() == authHash.hexdigest()):
        valid = 1
    return valid

def genLoginBlock(auth, MAC, authHash):
    loginBlockHash = None
    if(auth == 1):
        concat = MAC + authHash.hexdigest() + str(datetime.now())
        loginBlockHash = minePassword.getHash(concat)
    return loginBlockHash
    
def checkLoginBlock(loginBlock):
    loginSuccess = 0
    try:
        digest = loginBlock.hexdigest()
        loginSuccess = 1
    except:
        print("Authetication Failed")
    
    return loginSuccess
    
if __name__ == "__main__":
    main()
