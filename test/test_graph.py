import unittest
from src.graph import *


class TestArrays(unittest.TestCase):

    def build_graph(self):
        g = Graph(5)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)
        return g

    def test_graph_bfs(self):
        g = self.build_graph()

        self.assertEqual('02143', bfs(g, 0))

    def test_graph_dfs(self):
        g = self.build_graph()

        allowed_results = ['02143', '01342']
        self.assertIn(their_dfs(g, 0), allowed_results)

    def test_number_of_nodes(self):
        g = self.build_graph()

        self.assertEqual(1, number_of_nodes(g, 1))

    def test_find_all_paths(self):
        g = Graph(6)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)
        g.add_edge(2, 5)
        g.add_edge(3, 5)
        g.add_edge(4, 5)

        result = [[0, 2, 5],
                  [0, 1, 4, 5],
                  [0, 1, 3, 5]]

        self.assertEqual(result, find_all_paths(g, 0, 5))

    def test_transpose(self):
        g = self.build_graph()
        t = Graph(5)
        g.add_edge(1, 0)
        g.add_edge(2, 0)
        g.add_edge(3, 1)
        g.add_edge(4, 1)
        transposed = their_transpose(g)
        # transposed = transpose(g)
        # self.assertEqual(t, )
        transposed.print_graph()