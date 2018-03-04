import time
import itertools

import data
import solution


class ConstructionHeuristic:
    def __init__(self,instance):
        self.instance = instance

    def construct(self, time_left):
        return(self.canonical_solution(time_left))
        #return(self.saving_heuristic(time_left))

    def calculate_saving(self,i,j):
        return self.instance.distance_idx(i,j)-self.instance.distance_idx(i,0)-self.instance.distance_idx(j,0)

    def canonical_solution(self, time_left):
        sol = solution.Solution(self.instance)
        t0 = time.clock()
        route = [0]
        q=0
        for i in range(1,len(self.instance.nodes)): # we bypass the depot 0
            if q+self.instance.nodes[i]["rq"] <= self.instance.capacity:
                q+=self.instance.nodes[i]["rq"]
                route += [i]
            else:
                sol.routes += [route+[0]]
                route = [0,i]
                q=self.instance.nodes[i]["rq"]
            if time.clock() - t0 > time_left:
                sys.stdout.write("Time expired")
                return sol
        sol.routes += [route+[0]]
        return sol

    def saving_heuristic(self, time_left):
        routes={}
        idx = 0
        for i in range(1,len(self.instance.nodes)):
            routes[idx] = [0,i,0]
            idx+=1

        changed=True
        while (changed):
            changed=False
            savings=dict()
            for r1,r2 in itertools.combinations(routes.keys(),2):
                i=routes[r1][-2]
                j=routes[r2][1]
                savings.update({(i,j,r1,r2):self.calculate_saving(i,j)})
                i=routes[r2][-2]
                j=routes[r1][1]
                savings.update({(i,j,r2,r1):self.calculate_saving(i,j)})

            for i,j,r1,r2 in sorted(savings, key=savings.get):
                if r1 not in routes:
                    for r in routes.keys():
                        r1 = r if i==routes[r][-2] or j==routes[r][-2] else None
                if r2 not in routes:
                    for r in routes.keys():
                        r2 = r if j==routes[r][1] or i==routes[r][1] else None
                if r1 is None or r2 is None or r1==r2:
                    continue
                q=0
                for r in routes[r1][1:-1]:
                    q+=self.instance.nodes[r]["rq"]
                for r in routes[r2][1:-1]:
                    q+=self.instance.nodes[r]["rq"]
                if q <= self.instance.capacity:
                    changed=True
                    routes[idx]=routes[r1][:-1]+routes[r2][1:]
                    idx+=1
                    del routes[r1]
                    del routes[r2]

        sol = solution.Solution(self.instance)
        sol.routes=[routes[r] for r in routes]
        return sol
