from optimizer.node import Node
from optimizer.queue import PriorityQueue
from optimizer.utils import memoize
import random
import sys
import numpy as np

# Best First Search 
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
  
# A* algorithm 
def astar_search(problem, h=None, display=False):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n), display)

# Simulated Annealing algorithm
def exp_schedule(k=20, lam=0.005, limit=100):
    """One possible schedule function for simulated annealing"""
    return lambda t: (k * np.exp(-lam * t) if t < limit else 0)

def simulated_annealing(graph_problem, schedule=exp_schedule()):
    """[Figure 4.5] Returns node"""
    current = Node(graph_problem.initial)
    best_path = []
    best_distance = graph_problem.value(current)
    best_path.append(current)
    for t in range(sys.maxsize):
        T = schedule(t)
        if T == 0:
            print("\n returned " + str(best_path) + " because T equals " + str(T) + " at a distance of " + str(best_distance))
            return current
        neighbors = current.expand(graph_problem)
        if not neighbors:
            print("\n returned " + str(best_path) + " with a T of " + str(T) + " because it had no neighbors.")
            return current
        next_choice = random.choice(neighbors)
        delta_e = graph_problem.value(next_choice.state) - graph_problem.value(current.state)
        if delta_e < 0 :
            current = next_choice
            if not best_path.__contains__(current):
                best_path.append(current)
                best_distance+=graph_problem.value(current)
            print("\n analyzing" + str(current) + " at a T of " + str(T) + " and a delta_e of " + str(delta_e)
            + " resulting in " + str(best_path) + " and a distance of " + str(best_distance))

