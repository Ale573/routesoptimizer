from optimizer.graphProblem import GraphProblem
from optimizer.graph import UndirectedGraph
from optimizer.search import astar_search
from optimizer.search import simulated_annealing
from optimizer.problem import Problem



class GraphSearchAgent:
    """
    Modified from [Figure 3.1]
    Abstract framework for a problem-solving agent.
    """
    def __init__(self, initial_state=None, goal=None, map_dict=None, locations_dict=None, speed=1):
        """(Modified) State is an abstract representation of the state
        of the world, and seq is the list of actions required
        to get to a particular state from the initial state(root).
        The environment is a given graph"""
        self.state = initial_state
        self.goal = goal
        self.map_dict = map_dict
        self.locations = locations_dict
        self.speed = speed
        self.seq = []
        self.problem = self.create_problem()

    def __call__(self, percept="A*"):
        """[Figure 3.1] (Modified) With goal, problem, and state
        search for a sequence of actions to solve it.
        Percept should be the name of the algorithm to implement in the search"""
        if not self.seq:
            self.seq = self.search(percept)
            if not self.seq:
                return None
        return self.seq

    def create_problem(self):
        map_time = self.change_distance_by_time(self.map_dict, self.speed)
        graph_map = UndirectedGraph(map_time)
        graph_map.locations = self.locations
        return GraphProblem(self.state, self.goal, graph_map, self.speed)
    
    def search(self, algorithm='A*'):
        """Use the keywords "A*" or "Annealing" to choose the search algorithm. By default it will search using both"""
        if algorithm=='A*':
            return astar_search(self.problem).solution()
        elif algorithm=='Annealing':
            return None #simulated_annealing(self.problem)

    def change_distance_by_time(self, map_dict, speed):
        map_time = {}
        for city in map_dict:
            connections = {}
            for neigthbor in map_dict[city]:
                connections[neigthbor] = (map_dict[city][neigthbor]) / speed # distance / speed (km / km/h)
            map_time[city] = connections
        return map_time


