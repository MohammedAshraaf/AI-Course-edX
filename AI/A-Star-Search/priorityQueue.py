import heapq


# For the Frontier Characteristics
class PriorityQueue:
    # initialize the frontier
    def __init__(self):
        # list for the elements
        self.elements = []
        # set to check if the elements exist in the frontier
        self.elements_unique = set()

    # add element to the frontier
    def put(self, item, priority):
        self.elements_unique.add(item)
        heapq.heappush(self.elements, (priority, item))

    # remove element from the frontier
    def get(self):
        priority, item = heapq.heappop(self.elements)
        self.elements_unique.remove(item)
        return item

    # check if it's empty
    def not_empty(self):
        return len(self.elements) > 0

    # check if element is in the frontier
    def in_frontier(self, item):
        return item in self.elements_unique


