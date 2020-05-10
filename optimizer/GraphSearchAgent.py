from optimizer import *

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
        """State is an abstract representation of the state
        of the world, and seq is the list of actions required
        to get to a particular state from the initial state(root).
        The environment is a given graph"""

        self.state = initial_state
        self.goal = goal
        self.problem = GraphProblem(state, goal, environment)
        self.seq = []

    def __call__(self, percept):
        """[Figure 3.1] (Modified) With goal, problem, and state
        search for a sequence of actions to solve it.
        Percept should be the name of the algorithm to implement in the search"""
        if not self.seq:
            self.seq = self.search(self.problem, percept)
            if not self.seq:
                return None
        return self.seq
    
    def search(self, algorithm):
        """Use the keywords "A*" or "Annealing" to choose the search algorithm. By default it will search using both"""
        if algorithm=="A*":
            return astar_search(self.problem)
        elif algorithm=="Annealing":
            return simulated_annealing(self.problem)
        else:
            return None



