from optimizer.graphProblem import GraphProblem
from optimizer.graph import UndirectedGraph
from optimizer.search import astar_search, simulated_annealing
from optimizer.problem import Problem
from optimizer.GraphSearchAgent import GraphSearchAgent
from optimizer.utils import map_to_dict, map_coordenates


if __name__ == "__main__":


    agent1 = GraphSearchAgent('WA', 'DC', 'USAMap.csv', 45)

    agent1_astar = agent1.__call__('A*')
    agent1_simulated_annealing = agent1.__call__('Annealing')

    print("Agent has discovered the path", agent1_astar[0],
          "with a time of", int(agent1_astar[1]), 
          "hours using A*.")
          
    print("Agent has discovered the path", agent1_simulated_annealing[0],
          "with a time of", int(agent1_simulated_annealing[1]), 
          "hours using Simulated Annealing.")

    #agent4= GraphSearchAgent('Aguadilla', 'SanGerman', 'PRMap.csv')
    #print("Agent has discovered the path "+ str(agent4.__call__('A*')) + " using A*.")
    #print("Agent has discovered the path " + str(agent4.__call__('Annealing')) + " using Annealing.") 