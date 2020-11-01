import unittest
from src.graph2 import *


class TestArrays(unittest.TestCase):

    def build_graph(self):
        g = Graph2()
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(1, 3)
        g.add_edge(1, 4)
        return g

    def test_graph_bfs(self):
        g = self.build_graph()

        allowed_results = ['02143', '02134']
        self.assertIn(bfs(g, 0), allowed_results)

    def test_graph_dfs(self):
        g = self.build_graph()

        allowed_results = ['02143', '01342']
        self.assertIn(dfs(g, 0), allowed_results)

    # def test_number_of_nodes(self):
    #     g = self.build_graph()
    #
    #     self.assertEqual(1, number_of_nodes(g, 1))
    #
    def test_find_all_paths(self):
        g = Graph2()
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
        actual = find_all_paths(g, 0, 5)
        for path in actual:
            self.assertIn(path, result, f'path {path} not found in {result}')

    # def test_transpose(self):
    #     g = self.build_graph()
    #     t = Graph(5)
    #     g.add_edge(1, 0)
    #     g.add_edge(2, 0)
    #     g.add_edge(3, 1)
    #     g.add_edge(4, 1)
    #     transposed = their_transpose(g)
    #     # transposed = transpose(g)
    #     # self.assertEqual(t, )
    #     transposed.print_graph()