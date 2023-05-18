import queue


class Graph_ucs:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_edge(self, node1, node2, cost):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append((node2, cost))
        if not self.directed:
            self.graph[node2].append((node1, cost))

    def search(self, start, goals):
        visited = set()
        pq = queue.PriorityQueue()
        pq.put((0, start, []))

        while not pq.empty():
            cost, node, path = pq.get()

            if node in goals:
                return path + [node], node, cost

            if node not in visited:
                visited.add(node)
                for neighbor, edge_cost in self.graph[node]:
                    pq.put((cost + edge_cost, neighbor, path + [node]))

        return None, None, None

    @staticmethod
    def print_path(path):
        if path:
            print(' -> '.join(path))
        else:
            print('No path found.')
