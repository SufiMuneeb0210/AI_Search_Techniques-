from queue import PriorityQueue


class Graph_bestfs:
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

    def search(self, S, goal_nodes):
        Queue = PriorityQueue()
        Queue.put((self.heuristics[S], S))
        parents = {S: None}
        while not Queue.empty():
            CurrentCost, CurrentNode = Queue.get()
            CurrentCost = 0
            if CurrentNode in goal_nodes:
                path = []
                while CurrentNode:
                    path.append(CurrentNode)
                    if CurrentNode != S:
                        CurrentCost = CurrentCost + \
                            self.heuristics[CurrentNode]
                    CurrentNode = parents[CurrentNode]

                path.reverse()
                return path, goal_nodes, CurrentCost

            for child_node in self.graph[CurrentNode]:
                if child_node not in parents:
                    parents[child_node] = CurrentNode
                    Queue.put((self.heuristics[child_node], child_node))

        return None, None, None

    @staticmethod
    def print_path(path):
        if path:
            print(' -> '.join(path))
        else:
            print('No path found.')


# if __name__ == '__main__':
#     g = Graph_bestfs()
#     g.add_edge('S', 'A', 1)
#     g.add_edge('S', 'B', 5)
#     g.add_edge('A', 'C', 2)
#     g.add_edge('A', 'D', 3)
#     g.add_edge('B', 'E', 4)
#     g.add_edge('B', 'F', 6)
#     g.add_edge('C', 'G', 7)
#     g.add_edge('D', 'G', 8)
#     g.add_edge('E', 'G', 9)
#     g.add_edge('F', 'G', 10)
#     g.set_heuristic({'S': 10, 'A': 9, 'B': 7, 'C': 8,
#                      'D': 7, 'E': 6, 'F': 5, 'G': 0})
#     path, cost = g.search('S', {'G'})
#     g.print_path(path)
#     print('Cost: {}'.format(cost))
