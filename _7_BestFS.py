from collections import deque


class Graph_bestfs:
    def __init__(self, directed=False):
        self.graph = {}
        self.huristics = {}
        self.directed = directed

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append((node2, weight))
        if not self.directed:
            self.graph[node2].append((node1, weight))


    def set_huristics(self, heuristics={}):
        self.heuristics = heuristics
        
    
    @staticmethod
    def print_path(path):
        if path:
            print(' -> '.join(path))
        else:
            print('No path found.')
