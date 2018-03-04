import sys
import matplotlib
import matplotlib.pyplot as plt

import data


class Solution:
    routes = []
    def __init__(self, instance):
        self.instance = instance
        # the initialization for the containers for your solutions representation here
        pass

    def valid_solution(self):
        visited = [False] * len(self.instance.nodes)
        #print(self.routes)
        for route in self.routes:
            q=0
            if route[0]!=route[-1] or route[0]!=0:
                sys.stdout.write("\nRoute malformed: {}\n".format(route))
                return False
            visited[route[0]]=True
            for r in route[1:-1]:
                q+=self.instance.nodes[r]["rq"]
                if q>self.instance.capacity:
                    sys.stdout.write("\nDemand {} exceeded capacity {} in route: {}\n".format(q,self.instance.capacity,route))
                    return False
                if not visited[r]:
                    visited[r]=True
                else:
                    sys.stdout.write("\nNode {} is visited more than once\n".format(r))
                    return False
        if not all(visited):
            sys.stdout.write("\nSome node not visited\n")
            return False
        return(True)

    def cost(self):
        self.cost=0
        for route in self.routes:
            self.cost = sum(self.instance.distance_idx(route[i], route[i+1]) for i in range(len(route)-1))
        return(self.cost)

    def write_to_file(self, filename):
        with open(filename, "w") as filehandle:
            for route in self.routes:
                filehandle.write(",".join(map(lambda x: self.instance.nodes[x]["id"],route))+"\n")

    def plot_lines(self, points, style='bo-'):
        "Plot lines to connect a series of points."
        plt.plot([self.instance.nodes[p]["pt"].x for p in points], [self.instance.nodes[p]["pt"].y for p in points], style)
        plt.axis('scaled'); plt.axis('off')

    def plot_routes(self, outputfile_name=None):
        "routes is a list of routes (alternatively it can be a grand route).  The depot is red square."
        color = ["b","g","r","c","m","k"]
        c=0
        for route in self.routes:
            start = route[0]
            self.plot_lines(list(route) + [start], style=color[c]+"o-")
            self.plot_lines([start], 'rs') # Mark the start city with a red square
            c=(c+1) % len(color)
        if outputfile_name is None:
            plt.show()
        else:
            plt.savefig(outputfile_name)
