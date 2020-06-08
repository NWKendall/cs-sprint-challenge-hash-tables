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
    graph = {} # directed graph of tickets
    tickets_available = {} # {ticket : count} dict of ticket counts
    
    # Populate graph and tickets_available
    for source, destination in tickets:
        if source not in graph:
            graph[source] = [destination] # (destination airport, ticket_used) tuple
        else:
            graph[source].append(destination)
        
        ticket_name = "{}->{}".format(source, destination)
        if ticket_name not in tickets_available:
            tickets_available[ticket_name] = 1
        else:
            tickets_available[ticket_name] += 1
    
    # Sort destination airports by name
    for source in graph:
        graph[source].sort()
    
    # Find itinerary
    def dfs(source, so_far):
        global itinerary
        
        # If itinerary is alreay calculated, just return it (we are interested in the first itinerary)
        if itinerary:
            return itinerary

        # If we used up all tickets, save this itinerary
        elif len(so_far) == len(tickets)+1 and itinerary == None:  
            itinerary = so_far[:]
            
        elif source in graph:
            for destination in graph[source]:
                ticket_name = "{}->{}".format(source, destination)
                if tickets_available[ticket_name] > 0:
                    tickets_available[ticket_name] -= 1
                    so_far.append(destination)
                    dfs(destination, so_far)
                    so_far.pop()
                    tickets_available[ticket_name] += 1
    
    global itinerary
    itinerary = None        
    dfs('JFK', ["JFK"])
    return itinerary


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
