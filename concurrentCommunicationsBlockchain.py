#!/usr/bin/env python3

import minePassword
import authenticate
import clientKeyMining
import random
from blockchain import Block
from blockchain import Blockchain
from client import Client
from datetime import datetime

def main():
    #client information
    client1Serial = "987654321"
    client1MAC = "AA:BB:CC:DD:EE:FF:00:11"
    client2Serial = "021324354"
    client2MAC = "00:11:22:33:44:55:66:77"
    client3Serial = "111111111"
    client3MAC = "FF:EE:EE:DD:BB:EE:EE:FF"
    
    #initiate the Concurrent Communications Ledger
    ccl = Blockchain()
    
    #sessions
    client1, client2, sessionID, concat, ccb = initSession(client1Serial, client1MAC, client2Serial, client2MAC)
    addSession(ccl, sessionID, concat)
    #ccl.printBlockchain()
    
    #start Communications
    totalPackets = 10
    for p in range(totalPackets):
        #for demonstration, a random value is generated
        value = random.random()
        goingTo = client1
        comingFrom = client2
        sendPacket(ccb, goingTo, comingFrom, value)
        
    for p in range(totalPackets):
        #for demonstration, a random value is generated
        value = random.random()
        goingTo = client2
        comingFrom = client1
        sendPacket(ccb, goingTo, comingFrom, value)
        
    #Print the record of transactions
    ccb.printBlockchain()

#Initialize the session, get the session blockchain
def initSession(client1Serial, client1MAC, client2Serial, client2MAC):
    #for demonstration, we mine keys
    nonce, clientId1 = clientKeyMining.mineClientKey((client1Serial + client1MAC), 1)
    client1 = Client(clientId1, datetime.now())
    nonce, clientId2 = clientKeyMining.mineClientKey((client2Serial + client2MAC), 1)
    client2 = Client(clientId1, datetime.now())
    
    #Show Clients
    client1.printClient()
    client2.printClient()
    
    #Get the session timestamped by gateway
    sessionID, concat = getSessionID(client1.clientID, client2.clientID)
    ccb = Blockchain()
    return client1, client2, sessionID, concat, ccb
    
#Timestamp new session
def getSessionID(clientId1, clientId2):
    concat = clientId1.hexdigest() + clientId2.hexdigest() + str(datetime.now())
    sessionID = minePassword.getHash(concat)
    return sessionID, concat

#Increase Concurrent Communications Ledger
def addSession(ccl, hashVal, val):
    ccl.insert(hashVal, val)
    
def sendPacket(ccb, goingTo, comingFrom, value):
    hashVal = minePassword.getHash((str(value) + goingTo.clientID.hexdigest() + comingFrom.clientID.hexdigest()))
    value = "Going To: " + goingTo.clientID.hexdigest() + " Coming From: " + comingFrom.clientID.hexdigest() + " Value: " + str(value)
    ccb.insert(hashVal, value)

if __name__ == "__main__":
    main()
