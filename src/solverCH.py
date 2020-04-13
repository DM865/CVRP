import time
import sys

import solution


class ConstructionHeuristics:
    def __init__(self, instance):
        self.instance = instance

    def construct(self, time_left):
        return(self.canonical_solution(time_left))

    def canonical_solution(self, time_left):
        t0 = time.perf_counter()
        sol = solution.Solution(self.instance)
        route = [0]
        q = 0
        for i in range(1, len(self.instance.nodes)):  # we bypass the depot 0
            if q+self.instance.nodes[i]["rq"] <= self.instance.capacity:
                q += self.instance.nodes[i]["rq"]
                route += [i]
            else:
                sol.routes += [route+[0]]
                route = [0, i]
                q = self.instance.nodes[i]["rq"]
            if (time.perf_counter() - t0) > time_left:
                sys.stdout.write("Time expired")
                return sol
        sol.routes += [route+[0]]
        return sol
