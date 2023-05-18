from collections import deque


class Graph_ids:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_edge(self, node1, node2):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append(node2)
        if not self.directed:
            self.graph[node2].append(node1)

    def search(self, start, goals, max_depth):
        for depth in range(max_depth):
            path, node = self.depth_limited_search(start, goals, depth)
            print(f"Depth# {depth} :", end=" ")
            self.print_path(path)
            if path:
                return path, node

        return None, None

    def depth_limited_search(self, start, goals, limit):
        visited = set()
        stack = deque([(start, [])])

        while stack:
            node, path = stack.pop()

            if node in goals:
                return path + [node], node

            if node not in visited and len(path) < limit:
                visited.add(node)
                for neighbor in self.graph[node]:
                    stack.append((neighbor, path + [node]))

        return None, None

    @staticmethod
    def print_path(path):
        if path:
            print(' -> '.join(path))
        else:
            print('No path found.')
