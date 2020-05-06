import numpy as np
import csv

def get_data_from_csv(self):
    with open('tests/map2.csv', encoding='utf-8') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        result = []
        for row in readCSV:
            result.append(row)
        return result

def h(self, node):
        """h function is straight-line distance from a node's state to goal."""
        locs = getattr(self.graph, 'locations', None)
        if locs:
            if type(node) is str:
                return int(distance(locs[node], locs[self.goal]))

            return int(distance(locs[node.state], locs[self.goal]))
        else:
            return np.inf

def distance(a, b):
        """The distance between two (x, y) points."""
        xA, yA = a
        xB, yB = b
        return np.hypot((xA - xB), (yA - yB))

def is_in(elt, seq):
    """Similar to (elt in seq), but compares with 'is', not '=='."""
    return any(x is elt for x in seq)