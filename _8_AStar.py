from math import inf


class Graph_astar:
    def __init__(self, directed=True):
        self.graph = {}
        self.heuristics = {}
        self.directed = directed

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        if node2 not in self.graph:
            self.graph[node2] = {}

        self.graph[node1][node2] = weight
        if not self.directed:
            self.graph[node2][node1] = weight

    def set_heuristic(self, heuristics={}):
        self.heuristics = heuristics

    def search(self, start, setOfGoals):
        found, fringe, visited, path, cost = False, [
            (self.heuristics[start], start)], set([start]), [start], {start: 0}
        goal = 0
        while not found and len(fringe):
            current = fringe.pop(0)
            _, current = current
            if current in setOfGoals:
                found = True
                goal = current
                break
            for node in self.graph[current]:
                new_cost = cost[current] + self.graph[current][node]
                if node not in visited or cost[node] > new_cost:
                    visited.add(node)
                    path.append(node)
                    cost[node] = new_cost
                    fringe.append((new_cost + self.heuristics[node], node))
                    fringe.sort()
        if found:
            return path, goal, cost[goal]
        else:
            return None, inf

    @staticmethod
    def print_path(path):
        if path:
            print(' -> '.join(path))
        else:
            print('No path found.')
