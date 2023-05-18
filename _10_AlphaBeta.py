from collections import deque


class Graph_AlphaBeta:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append((node2, weight))
        if not self.directed:
            self.graph[node2].append((node1, weight))

    def search(self, start, goals):
        visited = set()
        queue = deque([(start, [], 0)])

        while queue:
            node, path, cost = queue.popleft()

            if node in goals:
                return path + [node], node

            if node not in visited:
                visited.add(node)
                for neighbor, weight in self.graph[node]:
                    queue.append((neighbor, path + [node], cost + weight))

        return None, None

    @staticmethod
    def print_path(path):
        if path:
            print(' -> '.join(path))
        else:
            print('No path found.')
