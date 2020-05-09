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
    cities = csv_data[0][1:]
    result = dict()
    for row in csv_data[1:]:
        connections = dict()
        index = 0
        for column in row[1:]:
            if int(column) != 0:
                connections[cities[index]] = column
            index += 1
        result[row[0]] = connections
    return result

def probability(p):
    """Return true with probability p."""
    return p > random.uniform(0.0, 1.0)

def distance(a, b):
        """The distance between two (x, y) points."""
        xA, yA = a
        xB, yB = b
        return np.hypot((xA - xB), (yA - yB))

def is_in(elt, seq):
    """Similar to (elt in seq), but compares with 'is', not '=='."""
    return any(x is elt for x in seq)

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
