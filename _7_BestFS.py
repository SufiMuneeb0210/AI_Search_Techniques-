from collections import deque


class Graph_bestfs:
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

    @staticmethod
    def print_path(path):
        if path:
            print(' -> '.join(path))
        else:
            print('No path found.')

    def search(self, start, goal):
        visited = set()
        priority_queue = deque([(0, start, [])])
        while priority_queue:
            _, current_node, path = priority_queue.popleft()
            visited.add(current_node)

            if current_node == goal:
                return path + [current_node]

            neighbors = self.graph.get(current_node, [])
            neighbors.sort(key=lambda x: self.heuristic(x[0], goal))
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    priority_queue.append(
                        (self.heuristic(neighbor, goal), neighbor, path + [current_node]))

        return []

    def heuristic(self, node, goal):
        x1, y1 = node
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)
