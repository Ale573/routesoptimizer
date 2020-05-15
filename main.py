from optimizer.graphProblem import GraphProblem
from optimizer.graph import UndirectedGraph
from optimizer.search import astar_search, simulated_annealing
from optimizer.problem import Problem
from optimizer.GraphSearchAgent import GraphSearchAgent
from optimizer.utils import map_to_dict, map_coordenates


if __name__ == "__main__":

    agent1= GraphSearchAgent('WA', 'DC', 'USAMap.csv', 45)
    agent1_result = agent1.__call__('A*')
    print("Agent has discovered the path", agent1_result[0], "with time of", agent1_result[1], "hours using A*.")
    
    agent2= GraphSearchAgent('WA', 'DC', 'USAMap.csv', 45)
    agent2_result = agent2.__call__('Annealing')
    print("Agent has discovered the path", agent2_result, "using Simulated Annealing.")

    agent3= GraphSearchAgent('Aguadilla', 'SanGerman', 'PRMap.csv', 45)
    agent3_result = agent3.__call__('A*')
    print("Agent has discovered the path", agent3_result[0], "with time of", agent3_result[1], "hours using A*.")
    
    agent4= GraphSearchAgent('Aguadilla', 'SanGerman', 'PRMap.csv', 45)
    agent4_result = agent4.__call__('Annealing')
    print("Agent has discovered the path", agent4_result, "using Simulated Annealing.")   