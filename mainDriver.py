#!/usr/bin/env python3

#reference: https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python

import minePassword
import authenticate
import clientKeyMining

class Block:
    def __init__(self, inputVal, concat, clientKey, next=None):
        self.inputVal = inputVal
        self.concat = concat
        self.clientKey = clientKey
        self.next = next
        
class Blockchain:
    def __init__(self):
        self.head = None
        
    def insert(self, inputVal, concat, clientKey):
        newNode = Block(inputVal, concat, clientKey)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode
            
    def printBlockchain(self):
        print("\n*****Printing Login Ledger*****")
        current = self.head
        while(current):
            print("\n*****Login Record*****")
            print("Hashed Value: " + str(current.inputVal.hexdigest()))
            print("Value: " + str(current.concat))
            print("Client Key: " + str(current.clientKey.hexdigest()))
            current = current.next

def main():
    NUM_USERS = 5
    networkHash, authHash = getPassword()
    loginLedger = Blockchain()
    for x in range(NUM_USERS):
        concat = login(loginLedger, x, networkHash, authHash, NUM_USERS)
    loginLedger.printBlockchain()
        
def login(loginLedger, x, networkHash, authHash, NUM_USERS):
    try:
        loginBlock, concat = authenticate.main(networkHash, authHash)
        loginBlock.hexdigest()
        print("\n*****Add Auth " + str(x) + " Login Ledger*****")
        acceptance = calcAcceptance(NUM_USERS)
        nonce, key = clientKeyMining.mineClientKey(concat, int(acceptance))
        loginLedger.insert(loginBlock, concat, key)
        print("Login Record Hash: " + loginBlock.hexdigest())
        print("Client " + str((x+1)) + " Key: " + key.hexdigest())
        return concat
    except Exception:
        traceback.print_exc()
        print("Exiting")
    
def getPassword():
    minedPassword, networkHash, authHash = minePassword.main()
    return networkHash, authHash
    
def calcAcceptance(num_users):
    return (2 ** num_users) / (num_users * num_users)
    
if __name__ == "__main__":
    main()
