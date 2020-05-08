import optimizer.node
import optimizer.graphProblem
import references.utils
import sys
import random
import numpy as np

class SimulatedAnnealing: 

    def __init__(self):
        super().__init__()

    def exp_schedule(self, k=20, lam=0.005, limit=100):
        """One possible schedule function for simulated annealing"""
        return lambda t: (k * np.exp(-lam * t) if t < limit else 0)

    def search(self, graph_problem, schedule=exp_schedule()):
        """[Figure 4.5] Returns node"""
        current = Node(graph_problem.initial)
        best_path = []
        best_distance = graph_problem.value(current)
        best_path.append(current)
        for t in range(sys.maxsize):
            T = schedule(t)
            if T == 0:
                print("\n returned " + str(best_path) + " because T equals " + str(T) + " at a distance of " + str(best_distance))
                return current
            neighbors = current.expand(graph_problem)
            if not neighbors:
                print("\n returned " + str(best_path) + " with a T of " + str(T) + " because it had no neighbors.")
                return current
            next_choice = random.choice(neighbors)
            delta_e = graph_problem.value(next_choice.state) - graph_problem.value(current.state)
            if delta_e < 0 :
                current = next_choice
                if not best_path.__contains__(current):
                    best_path.append(current)
                    best_distance+=graph_problem.value(current)
                print("\n analyzing" + str(current) + " at a T of " + str(T) + " and a delta_e of " + str(delta_e)
                + " resulting in " + str(best_path) + " and a distance of " + str(best_distance))

