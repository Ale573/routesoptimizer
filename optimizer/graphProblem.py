from optimizer.problem import Problem
from optimizer.utils import distance
import numpy as np
import geopy.distance

class GraphProblem(Problem):
    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph, speed):
        super().__init__(initial, goal)
        self.graph = graph
        self.speed = speed

    def actions(self, A):
        """The actions at a graph node are just its neighbors."""
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def path_cost(self, cost_so_far, A, action, B=None):
        return cost_so_far + (self.graph.get(A, B) or np.inf)

    def find_min_edge(self):
        """Find minimum value of edges."""
        m = np.inf
        for d in self.graph.graph_dict.values():
            local_min = min(d.values())
            m = min(m, local_min)
        return m

    def value(self, node1, node2):
        """Sets the value of the state of the nodes as the direct distance between the node1 and the goal,
        and the distance between node1 and its previous node (node2) as provided by the function h(node)"""
        return self.h(node1) + self.graph.get(node1, node2)

    def h(self, node):
        """h function is straight-line distance from a node's state to goal. Using latitude and longitude."""
        locs = getattr(self.graph, 'locations', None)
        if locs:
            if type(node) is str:
                return (geopy.distance.geodesic(locs[node.state], locs[self.goal]).km / self.speed)
            return (geopy.distance.geodesic(locs[node.state], locs[self.goal]).km / self.speed)
        else:
            return np.inf
