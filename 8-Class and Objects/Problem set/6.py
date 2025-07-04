'''
6. Can you change the self-parameter inside a class to something else (say
"harry"). Try changing self to "slf" or "harry" and see the effects.
'''

from random import randint

class Train:
    def __init__(slf, trainNo):  # Fixed method name "__init__"
        slf.trainNo = trainNo

    def book(self, fro, to):
        print(f" Ticket booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f" Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f" Ticket fare in train no: {self.trainNo} from {fro} to {to} is ₹{randint(222, 5555)}")

# Example usage
t = Train(12399)
t.book("Rampur", "Delhi")  # Book a ticket
t.getStatus()  # Check train status
t.getFare("Rampur", "Delhi")  # Get ticket fare




#Outpit will be intact but it will decrease the readability of the code