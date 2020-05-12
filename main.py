from optimizer.graphProblem import GraphProblem
from optimizer.graph import UndirectedGraph
from optimizer.search import astar_search
from optimizer.search import simulated_annealing
from optimizer.problem import Problem

from optimizer.graphSearchAgent import GraphSearchAgent

from optimizer.utils import map_to_dict
from optimizer.utils import map_coordenates

#import geopy.distance
#geopy.distance.geodesic(row, column).km

# Romania Map to Graph
romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))

# Romania Locations for the Grid  
romania_map.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))

def main():
    

    #Search agent
    agent1= GraphSearchAgent('Arad', 'Bucharest', romania_map)
    print("Agent has discovered the path "+ str(agent1.__call__('A*')) + " using A*.")
    
    agent2= GraphSearchAgent('Arad', 'Bucharest', romania_map)
    print("Agent has discovered the path "+ str(agent2.__call__('Annealing')) + " using Annealing.")

    agent3= GraphSearchAgent('WA', 'DC', 'USAMap.csv')
    print("Agent has discovered the path " + str(agent3.__call__('A*')) + " using A*.")
    print("Agent has discovered the path " + str(agent3.__call__('Annealing')) + " using Annealing.")

    agent4= GraphSearchAgent('Aguadilla', 'SanGerman', 'PRMap.csv')
    print("Agent has discovered the path "+ str(agent4.__call__('A*')) + " using A*.")
    print("Agent has discovered the path " + str(agent4.__call__('Annealing')) + " using Annealing.")    

if __name__ == "__main__":
    main()