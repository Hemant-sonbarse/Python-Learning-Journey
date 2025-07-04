'''
5. Write a class Train which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways.
'''
from random import randint

class Train:
    def __init__(self, trainNo):  # Fixed method name "__init__"
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"🎟️ Ticket booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"🚆 Train no: {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"💰 Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")

# Example usage
t = Train(12399)
t.book("Rampur", "Delhi")  # Book a ticket
t.getStatus()  # Check train status
t.getFare("Rampur", "Delhi")  # Get ticket fare
