from optimizer.graphProblem import GraphProblem
from optimizer.graph import UndirectedGraph
from optimizer.search import astar_search, simulated_annealing
from optimizer.problem import Problem
from optimizer.GraphSearchAgent import GraphSearchAgent
from optimizer.utils import map_to_dict, map_coordenates

from tests import romania

def main():
    # USA Map
    # Distance map
    usa_dict = map_to_dict(csv_map='USAMap.csv')
    # Location map
    usa_dict_locations = map_coordenates(csv_map='USAMap.csv')
    # Initial state and goal state 
    initial_usa = 'WA'
    goal_usa = 'DC'

    USA_Agent = GraphSearchAgent(initial_usa, goal_usa, usa_dict, usa_dict_locations, 50)
    print("Agent has discovered the path "+ str(USA_Agent.__call__('A*')) + " using A*.")
    
    #PR MAP
    # Distance map
    pr_dict = map_to_dict(csv_map='PRMap.csv')
    # Location map
    pr_dict_locations = map_coordenates(csv_map='PRMap.csv')
    # Initial state and goal state 
    initial_pr = 'Aguadilla'
    goal_pr = 'San Germán'
    
    PR_Agent = GraphSearchAgent(initial_pr, goal_pr, pr_dict, pr_dict_locations, 45)
    print("Agent has discovered the path "+ str(PR_Agent.__call__('A*')) + " using A*.")

    # ROMANIA MAP
    initial_romania = 'Arad'
    goal_romania = 'Bucharest'
    romania_problem = GraphProblem(initial_romania, goal_romania, romania.romania_map, 1, True)

    romania_result = astar_search(romania_problem).solution()

    print('Path from %s to %s is: %s using A*.' % (initial_romania, goal_romania, romania_result))    

if __name__ == "__main__":
    main()