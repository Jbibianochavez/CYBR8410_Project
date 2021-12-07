class Client:
    def __init__(self, clientID, timeStamp):
        self.clientID = clientID
        self.timeStamp = timeStamp
    
    def printClient(self):
        print("\n***** Printing Client******")
        print("ID: " + self.clientID.hexdigest())
        print("Init Time: " + str(self.timeStamp))
