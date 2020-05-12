from optimizer.graphProblem import GraphProblem
from optimizer.graph import UndirectedGraph
from optimizer.search import astar_search, simulated_annealing
from optimizer.problem import Problem
from optimizer.GraphSearchAgent import GraphSearchAgent
from optimizer.utils import map_to_dict, map_coordenates


if __name__ == "__main__":


    agent1 = GraphSearchAgent('WA', 'DC', 'USAMap.csv', 45)
    print("Agent has discovered the path " + str(agent1.__call__('A*')) + " using A*.")
    print("Agent has discovered the path " + str(agent1.__call__('Annealing')) + " using Annealing.")

    #agent4= GraphSearchAgent('Aguadilla', 'SanGerman', 'PRMap.csv')
    #print("Agent has discovered the path "+ str(agent4.__call__('A*')) + " using A*.")
    #print("Agent has discovered the path " + str(agent4.__call__('Annealing')) + " using Annealing.") 