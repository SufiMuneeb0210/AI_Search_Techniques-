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

    def search(self, start_node, goal_node):
        # Initialize the sets of visited nodes for both forward and backward search
        ForwardVisited = set()
        BackwardVisited = set()
        ForwardVisited.add(start_node)
        BackwardVisited.add(goal_node)

        # Initialize the sets of Same level nodes for both forward and backward search
        ForwardSiblings = [start_node]
        BackwardSiblings = [goal_node]

        # Initialize the dictionaries to keep track of the parent nodes for both forward and backward search
        ForwardParent = {start_node: None}
        BackwardParent = {goal_node: None}

        # Iterate until a common node is found or both search lists are empty
        while ForwardSiblings or BackwardSiblings:
            # Expand the Current Siblings of the forward search upto 1 level
            ForwardNextSibling = []
            for u in ForwardSiblings:
                for v in self.graph[u]:
                    if v not in ForwardVisited:
                        ForwardParent[v] = u
                        ForwardVisited.add(v)
                        ForwardNextSibling.append(v)
            ForwardSiblings = ForwardNextSibling
            # Check if any of the nodes in the forward search is already visited by the backward search
            for u in ForwardSiblings:
                if u in BackwardVisited:
                    return self.getpath(ForwardParent, BackwardParent, u)

            # Expand the Current Siblings of the backward search upto 1 level
            BackwardNextSibling = []
            for u in BackwardSiblings:
                for v in self.graph[u]:
                    if v not in BackwardVisited:
                        BackwardParent[v] = u
                        BackwardVisited.add(v)
                        BackwardNextSibling.append(v)
            BackwardSiblings = BackwardNextSibling
            # Check if any of the nodes in the backward search is already visited by the forward search
            for u in BackwardSiblings:
                if u in ForwardVisited:
                    return self.getpath(ForwardParent, BackwardParent, u)
        return None

    def getpath(self, ForwardParent, BackwardParent, child):
        ForwardPath = []
        while child:
            ForwardPath.append(child)
            # get parent against a child from dictionary
            child = ForwardParent[child]

        BackwardPath = []
        while child:
            BackwardPath.append(child)
            # get parent against a child from  dictionary
            child = BackwardParent[child]
        BackwardPath.reverse()
        path = ForwardPath + BackwardPath
        path.reverse()
        return (path)

    @staticmethod
    def print_path(path):
        if path:
            print(' -> '.join(path))
        else:
            print('No path found.')


# if __name__ == '__main__':
#     graph = Graph_bds(directed=True)
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
#     graph.add_edge('K', 'Q')
#     graph.add_edge('L', 'R')
#     graph.add_edge('L', 'S')
#     graph.add_edge('N', 'T')
#     graph.add_edge('N', 'U')
#     graph.add_edge('P', 'V')
#     graph.add_edge('P', 'W')
#     graph.add_edge('R', 'X')
#     graph.add_edge('R', 'Y')

#     path = graph.search('A', 'Y')
#     graph.print_path(path)
