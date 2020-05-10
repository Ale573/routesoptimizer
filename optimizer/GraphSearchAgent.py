from optimizer.graphProblem import GraphProblem
from optimizer.graph import UndirectedGraph
from optimizer.search import astar_search
from optimizer.search import simulated_annealing
from optimizer.problem import Problem

from optimizer.utils import map_to_dict
from optimizer.utils import map_coordenates

class GraphSearchAgent:
    """
    Modified from [Figure 3.1]
    Abstract framework for a problem-solving agent.
    """
    state = None
    problem = None
    goal = None
    seq = [] 

    def __init__(self, initial_state=None, goal=None, environment= None):
        """(Modified) State is an abstract representation of the state
        of the world, and seq is the list of actions required
        to get to a particular state from the initial state(root).
        The environment is a given file that will turn into a graph"""

        self.state = initial_state
        self.goal = goal
        if isinstance(environment, str):
            #If given string of name of file
            #Map dictionary
            file_dict= map_to_dict(csv_map=environment)
            file_dict_locations = map_coordenates(csv_map=environment)
            # Dictionary to Graph
            file_map = UndirectedGraph(file_dict)
            file_map.locations = file_dict_locations
            self.problem = GraphProblem(initial_state, goal, file_map)
        else:
            #if given graph
            self.problem = GraphProblem(initial_state, goal, environment)

        self.seq = []

    def __call__(self, percept='A*'):
        """[Figure 3.1] (Modified) With goal, problem, and state
        search for a sequence of actions to solve it.
        Percept should be the name of the algorithm to implement in the search"""
        if not self.seq:
            self.seq = self.search(percept)
            if not self.seq:
                return None
        return self.seq
    
    def search(self, algorithm='A*'):
        """Use the keywords "A*" or "Annealing" to choose the search algorithm. By default it will search using both"""
        if algorithm=='A*':
            return astar_search(self.problem).solution()
        elif algorithm=='Annealing':
            return None #simulated_annealing(self.problem)




