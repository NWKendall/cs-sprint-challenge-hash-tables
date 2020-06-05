#  Hint:  You may not need all of these.  Remove the unused functions.
import random

class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets):
    """
    YOUR CODE HERE
    """
    # Your code here
    flights = {}
    journey = []
    for t in tickets:
        # populate dictionary
        flights[t.source] = t.destination
        
    def visit(tickets):
        while flights[tickets]:
            visit(flights[tickets].pop())
        journey.append(tickets)

    return journey[::-1]


trip = [Ticket("PIT", "ORD"),
        Ticket("XNA", "SAP"),
        Ticket("SFO", "BHM"),
        Ticket("FLG", "XNA"),
        Ticket("NONE", "LAX"),
        Ticket("LAX", "SFO"),
        Ticket("SAP", "SLC"),
        Ticket("ORD", "NONE"),
        Ticket("SLC", "PIT"),
        Ticket("BHM", "FLG")]


print(reconstruct_trip(trip))
# markov table ✅
# need dict to place tickets ✅
# populate dictionary with tickets ✅
# populate journey
# return array of locations (journey)
    # starts with None
    # Ends with None
    # Remove None from return array
