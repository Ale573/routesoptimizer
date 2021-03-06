from optimizer.node import Node
from optimizer.queue import PriorityQueue
from optimizer.utils import *
import random
import sys
import numpy as np

"""
Autorship: Aimacode Repository
URL: https://github.com/aimacode/aima-python
"""
# ----------------------- BEST FIRST SEARCH -----------------------
def best_first_graph_search(problem, f, display=False):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            if display:
                print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
            return node
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    return None
  

# ----------------------- A STAR -----------------------
def astar_search(problem, h=None, display=False):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n), display)


# ----------------------- SIMULATED ANNEALING -----------------------
def exp_schedule(k=20, lam=0.005, limit=100):
    """One possible schedule function for simulated annealing"""
    return lambda t: (k * np.exp(-lam * t) if t < limit else 0)

def simulated_annealing(problem, schedule=exp_schedule()):
    """ This version returns all the states encountered in reaching 
    the goal state."""
    states = []
    current = Node(problem.initial)
    current_value = problem.h(current)
    for t in range(sys.maxsize):
        T = problem.h(current)
        if not states.__contains__(current.state):
            states.append(current.state)
            #print("Analyzing " + str(states) + ". T equals " + str(T))
        if T == 0:
            #print("Returned " + str(states) + ". T equals " + str(T))
            return states
        neighbors = current.expand(problem)
        if not neighbors:
            return current.state
        next_choice = random.choice(neighbors)
        delta_e = problem.h(next_choice) -current_value
        if delta_e < 0 or probability(np.exp(delta_e / T)):
            current_value= problem.h(next_choice)
            current = next_choice

