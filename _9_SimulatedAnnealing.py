import math
import random


class Graph_SA:
    def __init__(self, directed=True):
        self.graph = {}
        self.directed = directed

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        if node2 not in self.graph:
            self.graph[node2] = {}

        self.graph[node1][node2] = weight
        if not self.directed:
            self.graph[node2][node1] = weight

    def get_cost(self, path):
        cost = 0
        for i in range(len(path) - 1):
            node1 = path[i]
            node2 = path[i + 1]
            if node1 in self.graph and self.graph[node1].keys() and node2 in self.graph[node1]:
                cost += self.graph[node1][node2]
        return cost

    def search(self, start, goals, iterations=1000):
        self.print_graph()
        current = start
        path = [current]
        for i in range(iterations):
            T = math.exp(-i / iterations)
            neighbors = list(self.graph[current].keys()
                             ) if current in self.graph else []
            next_node = random.choice(neighbors) if neighbors else None
            delta = self.graph[current][next_node] if next_node else 0
            if delta < 0:
                current = next_node
                path.append(current)
            else:
                if next_node and random.random() < math.exp(-delta / T):
                    current = next_node
                    path.append(current)
            if current in goals:
                break
        cost = self.get_cost(path)
        return path, goals, cost

    @staticmethod
    def print_path(path):
        if path:
            print(' -> '.join(path))
        else:
            print('No path found.')

    def print_graph(self):
        print("The Graph printed as Dictionary:")
        for key, value in self.graph.items():
            print(key, ' : ', value)


# if __name__ == '__main__':
#     g = Graph_SA(directed=True)
#     g.add_edge('A', 'B', 3)
#     g.add_edge('A', 'C', 5)
#     g.add_edge('A', 'D', 8)
#     g.add_edge('B', 'C', 2)
#     g.add_edge('B', 'D', 4)
#     g.add_edge('C', 'D', 1)

#     path, goal, cost = g.search('A', 'D', iterations=1000)
#     g.print_path(path)
#     print('Cost:', cost)
