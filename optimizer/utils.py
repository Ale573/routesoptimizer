import numpy as np
import csv
import random

def get_data_from_csv(csv_map):
    with open('tests/' + csv_map, encoding='utf-8') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        result = []
        for row in readCSV:
            result.append(row)
        return result

def map_to_dict(csv_map):
    csv_data = get_data_from_csv(csv_map)
    cities = csv_data[0][2:]
    result = dict()
    for row in csv_data[1:]:
        connections = dict()
        index = 0
        for column in row[2:]:
            if float(column) != 0:
                connections[cities[index]] = eval(column)
            index += 1
        result[row[1]] = connections
    return result

def map_coordenates(csv_map):
    csv_data = get_data_from_csv(csv_map)
    cities = csv_data[0][2:]
    result = dict()
    index = 0
    for row in csv_data[1:]:
        for column in row[:1]:
            if index < len(cities):
                result[cities[index]] = eval(column)
            index += 1
    return result

def probability(p):
    """Return true with probability p."""
    return p > random.uniform(0.0, 1.0)

<<<<<<< HEAD
# ______________________________________________________________________________
# Grid Functions
def distance(a, b):
    """The distance between two (x, y) points."""
    xA, yA = a
    xB, yB = b
    return np.hypot((xA - xB), (yA - yB))

# ______________________________________________________________________________
# Misc Functions
=======
def distance(a, b):
        """The distance between two (x, y) points."""
        xA, yA = a
        xB, yB = b
        return np.hypot((xA - xB), (yA - yB))

def is_in(elt, seq):
    """Similar to (elt in seq), but compares with 'is', not '=='."""
    return any(x is elt for x in seq)
>>>>>>> e8610dfacd681602f271e290c910b23bbb3e2beb

def memoize(fn, slot=None, maxsize=32):
    """Memoize fn: make it remember the computed value for any argument list.
    If slot is specified, store result in that slot of first argument.
    If slot is false, use lru_cache for caching the values."""
    if slot:
        def memoized_fn(obj, *args):
            if hasattr(obj, slot):
                return getattr(obj, slot)
            else:
                val = fn(obj, *args)
                setattr(obj, slot, val)
                return val
    else:
        @functools.lru_cache(maxsize=maxsize)
        def memoized_fn(*args):
            return fn(*args)

    return memoized_fn
<<<<<<< HEAD

# ______________________________________________________________________________
# Queues: Stack, FIFOQueue, PriorityQueue
# Stack and FIFOQueue are implemented as list and collection.deque
# PriorityQueue is implemented here

class PriorityQueue:
    """A Queue in which the minimum (or maximum) element (as determined by f and
    order) is returned first.
    If order is 'min', the item with minimum f(x) is
    returned first; if order is 'max', then it is the item with maximum f(x).
    Also supports dict-like lookup."""

    def __init__(self, order='min', f=lambda x: x):
        self.heap = []
        if order == 'min':
            self.f = f
        elif order == 'max':  # now item with max f(x)
            self.f = lambda x: -f(x)  # will be popped first
        else:
            raise ValueError("Order must be either 'min' or 'max'.")

    def append(self, item):
        """Insert item at its correct position."""
        heapq.heappush(self.heap, (self.f(item), item))

    def extend(self, items):
        """Insert each item in items at its correct position."""
        for item in items:
            self.append(item)

    def pop(self):
        """Pop and return the item (with min or max f(x) value)
        depending on the order."""
        if self.heap:
            return heapq.heappop(self.heap)[1]
        else:
            raise Exception('Trying to pop from empty PriorityQueue.')

    def __len__(self):
        """Return current capacity of PriorityQueue."""
        return len(self.heap)

    def __contains__(self, key):
        """Return True if the key is in PriorityQueue."""
        return any([item == key for _, item in self.heap])

    def __getitem__(self, key):
        """Returns the first value associated with key in PriorityQueue.
        Raises KeyError if key is not present."""
        for value, item in self.heap:
            if item == key:
                return value
        raise KeyError(str(key) + " is not in the priority queue")

    def __delitem__(self, key):
        """Delete the first occurrence of key."""
        try:
            del self.heap[[item == key for _, item in self.heap].index(True)]
        except ValueError:
            raise KeyError(str(key) + " is not in the priority queue")
        heapq.heapify(self.heap)

# ______________________________________________________________________________
=======
>>>>>>> e8610dfacd681602f271e290c910b23bbb3e2beb
