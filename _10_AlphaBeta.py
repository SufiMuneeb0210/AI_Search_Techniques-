import math


class Graph_AlphaBeta:
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

    def alpha_beta_search(self, start, goal):
        visited = set()
        return self.max_value(start, goal, -math.inf, math.inf, visited, [start])

    def max_value(self, state, goal, alpha, beta, visited, path):
        if state == goal:
            return 0, path

        value = -math.inf
        for neighbor in self.graph[state]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                new_value, new_path = self.min_value(
                    neighbor, goal, alpha, beta, visited, new_path)
                visited.remove(neighbor)

                if new_value > value:
                    value = new_value
                    path = new_path
                if value >= beta:
                    return value, path
                alpha = max(alpha, value)
        return value, path

    def min_value(self, state, goal, alpha, beta, visited, path):
        if state == goal:
            return 0, path

        value = math.inf
        for neighbor in self.graph[state]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                new_value, new_path = self.max_value(
                    neighbor, goal, alpha, beta, visited, new_path)
                visited.remove(neighbor)

                if new_value < value:
                    value = new_value
                    path = new_path
                if value <= alpha:
                    return value, path
                beta = min(beta, value)
        return path, goal, value

    @staticmethod
    def print_path(path):
        if path:
            print(' -> '.join(path))
        else:
            print('No path found.')


# if __name__ == '__main__':
#     g = Graph_AlphaBeta(directed=True)
#     g.add_edge('A', 'B', 3)
#     g.add_edge('A', 'C', 5)
#     g.add_edge('A', 'D', 4)
#     g.add_edge('B', 'C', 5)
#     g.add_edge('B', 'D', 1)
#     g.add_edge('C', 'D', 2)

#     start = 'A'
#     goal = 'D'

#     value, path = g.alpha_beta_search(start, goal)
#     g.print_path(path)
#     print(value)
