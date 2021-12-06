#!/usr/bin/env python3

#reference: https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python

import minePassword
import authenticate

class Block:
    def __init__(self, inputVal, concat, next=None):
        self.inputVal = inputVal
        self.concat = concat
        self.next = next
        
class Blockchain:
    def __init__(self):
        self.head = None
        
    def insert(self, inputVal, concat):
        newNode = Block(inputVal, concat)
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
            print("Hashed Value: " + str(current.inputVal.hexdigest()))
            print("Value: " + str(current.concat))
            current = current.next

def main():
    networkHash, authHash = getPassword()
    loginLedger = Blockchain()
    for x in range(5):
        concat = login(loginLedger, x, networkHash, authHash)
    loginLedger.printBlockchain()
        
def login(loginLedger, x, networkHash, authHash):
    try:
        loginBlock, concat = authenticate.main(networkHash, authHash)
        loginBlock.hexdigest()
        print("\n*****Add Auth " + str(x) + " Login Ledger*****")
        loginLedger.insert(loginBlock, concat)
        print(loginBlock.hexdigest())
        return concat
    except Exception:
        #traceback.print_exc()
        print("Exiting")
    
def getPassword():
    minedPassword, networkHash, authHash = minePassword.main()
    return networkHash, authHash
    
if __name__ == "__main__":
    main()
