from collections import deque

# use this class code and provide me Graph_dls class code


class Graph_dls:
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

    def search(self, start, goals, limit):
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


# if __name__ == '__main__':
#     graph = Graph_dls()
#     graph.add_edge('A', 'B')
#     graph.add_edge('A', 'C')
#     graph.add_edge('B', 'D')
#     graph.add_edge('B', 'E')
#     graph.add_edge('C', 'F')
#     graph.add_edge('C', 'G')
#     graph.add_edge('D', 'H')
#     graph.add_edge('D', 'I')
#     graph.add_edge('F', 'J')
#     graph.add_edge('F', 'K')
#     graph.add_edge('G', 'L')
#     graph.add_edge('G', 'M')
#     graph.add_edge('H', 'N')
#     graph.add_edge('H', 'O')
#     graph.add_edge('K', 'P')

#     path, goal = graph.search('A', ['P'], 5)
#     graph.print_path(path)
