#!/usr/bin/env python3

#reference: https://www.educative.io/edpresso/how-to-create-a-linked-list-in-python

import minePassword
import authenticate
import clientKeyMining
from blockchain import Block
from blockchain import Blockchain

def main():
    NUM_USERS = 5
    networkHash, authHash = getPassword()
    loginLedger = Blockchain()
    clientIDLedger = Blockchain()
    for x in range(NUM_USERS):
        concat = login(clientIDLedger, loginLedger, x, networkHash, authHash, NUM_USERS)
    
    print("\n***** Printing Login Ledger *****")
    loginLedger.printBlockchain()
    print("\n***** Printing Client ID Ledger *****")
    clientIDLedger.printBlockchain()
        
def login(clientIDLedger, loginLedger, x, networkHash, authHash, NUM_USERS):
    try:
        loginBlock, concat = authenticate.main(networkHash, authHash)
        loginBlock.hexdigest()
        print("\n*****Add Auth " + str(x) + " Login Ledger*****")
        acceptance = calcAcceptance(NUM_USERS)
        nonce, key = clientKeyMining.mineClientKey(concat, int(acceptance))
        loginLedger.insert(loginBlock, concat)
        clientIDLedger.insert(key, concat)
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
