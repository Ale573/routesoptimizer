from optimizer.graphProblem import GraphProblem
from optimizer.graph import UndirectedGraph
from optimizer.search import astar_search
from optimizer.search import simulated_annealing
from optimizer.problem import Problem

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
    # Maps Dictionary
    usa_dict = map_to_dict(csv_map='USAMap.csv')
    usa_dict_locations = map_coordenates(csv_map='USAMap.csv')

    # Dictionary to Graph
    usa_map = UndirectedGraph(usa_dict)
    usa_map.locations = usa_dict_locations

    # Generate Problems
    romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
    usa_problem = GraphProblem('WA', 'DC', usa_map)

    # Testing both algorithm with distance

    # Romania 
    astar_result = astar_search(romania_problem).solution()
    # simulated_annealing_result = simulated_annealing(romania_problem)

    print('Path from Arad to Bucharest is:', astar_result)

    # USA s
    astar_result = astar_search(usa_problem).solution()

    print('Path from WA to DC is:', astar_result)
    

if __name__ == "__main__":
    main()