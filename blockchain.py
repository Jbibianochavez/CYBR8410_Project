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
        #print("\n*****Printing Ledger*****")
        current = self.head
        while(current):
            print("\n***** Record*****")
            print("Hashed Value: " + str(current.inputVal.hexdigest()))
            print("Value: " + str(current.concat))
            current = current.next
