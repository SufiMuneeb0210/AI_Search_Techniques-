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
        self.print_graph()
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
    
    def print_graph(self):
        print("The Graph printed as Dictionary:")
        for key, value in self.graph.items():
            print(key, ' : ', value)


# if __name__ == '__main__':
#     graph = Graph_ucs()
#     graph.add_edge('A', 'B', 1)
#     graph.add_edge('A', 'C', 2)
#     graph.add_edge('B', 'D', 5)
#     graph.add_edge('B', 'E', 6)
#     graph.add_edge('C', 'F', 7)
#     graph.add_edge('C', 'G', 8)
#     graph.add_edge('D', 'H', 9)
#     graph.add_edge('D', 'I', 10)
#     graph.add_edge('F', 'J', 11)
#     graph.add_edge('F', 'K', 12)
#     graph.add_edge('G', 'L', 13)
#     graph.add_edge('G', 'M', 14)
#     graph.add_edge('H', 'N', 15)
#     graph.add_edge('H', 'O', 16)
#     graph.add_edge('K', 'P', 17)

#     path, node, cost = graph.search('A', ['P'])
#     graph.print_path(path)
#     print(node, cost)
