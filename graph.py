#!/usr/bin/env python3
from collections import deque


class Node:

    def __init__(self, key):
        self.key = key
        self.is_visited = False
        self.adj_nodes = {}
        self.adj_weights = {}
        self.incoming_edges = 0

    def add_adjacent(self, node, weight):
        if node is None or weight is None:
            print('ERROR: Node or Weight can not be None')
        if node.key not in self.adj_nodes:
            self.adj_nodes[node.key] = node
            self.adj_weights[node.key] = weight
            node.incoming_edges += 1

    def remove_adjacent(self, node):
        if node is None:
            print('ERROR: Node can not be None')
        if node.key in self.adj_nodes:
            node.incoming_edges += 1
            del self.adj_nodes[node.key]

    def __repr__(self):
        return str(self.key)


class Graph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, key):
        if key is None:
            print('ERROR: Key can not be None')
        if key not in self.nodes:
            self.nodes[key] = Node(key)
        return self.nodes[key]

    def add_edge(self, key_a, key_b, weight):
        node_a = self.add_node(key_a)
        node_b = self.add_node(key_b)
        node_a.add_adjacent(node_b, weight)

    def breadth_first(self, node, visit_function):
        if node is None:
            return
        queue = deque()
        queue.append(node)
        node.is_visited = True
        while queue:
            node = queue.popleft()
            visit_function(node)
            for adj in node.adj_nodes.values():
                if not adj.is_visited:
                    queue.append(adj)
                    adj.is_visited = True

    def depth_first(self, node, visit_function):
        if node is None:
            return
        visit_function(node)
        node.is_visited = True
        for adj in node.adj_nodes.values():
            if not adj.is_visited:
                self.depth_first(adj, visit_function)

    def __repr__(self):
        return str(self.nodes.values())

if __name__ == '__main__':
    graph = Graph()
    for i in range(6):
        graph.add_node(i)
    graph.add_edge(0, 1, 5)
    graph.add_edge(0, 4, 3)
    graph.add_edge(0, 5, 2)
    graph.add_edge(1, 3, 5)
    graph.add_edge(1, 4, 4)
    graph.add_edge(2, 1, 6)
    graph.add_edge(3, 2, 7)
    graph.add_edge(3, 4, 8)
    print(graph)
    res_bfs = []
    graph.breadth_first(graph.nodes[0], res_bfs.append)
    print(res_bfs)  # 0,1,4,5,3,2
    for n in graph.nodes.values():
        n.is_visited = False
    res_dfs = []
    graph.depth_first(graph.nodes[0], res_dfs.append)
    print(res_dfs)  # 0,1,3,2,4,5
