from collections import deque


class Graph_bds:
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

    def search(self, start, goals):
        visited = set()
        queue1 = deque([(start, [])])
        queue2 = deque([(goals, [])])

        while queue1 and queue2:
            node1, path1 = queue1.popleft()
            node2, path2 = queue2.popleft()

            if node1 in visited:
                return path1 + [node1] + path2[::-1], node1

            if node2 in visited:
                return path1 + [node2] + path2[::-1], node2

            if node1 not in visited:
                visited.add(node1)
                for neighbor in self.graph[node1]:
                    queue1.append((neighbor, path1 + [node1]))

            if node2 not in visited:
                visited.add(node2)
                for neighbor in self.graph[node2]:
                    queue2.append((neighbor, path2 + [node2]))

        return None, None

    @staticmethod
    def print_path(path):
        if path:
            print(' -> '.join(path))
        else:
            print('No path found.')
