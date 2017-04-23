import unittest
import random
import connected_component


class CCTest(unittest.TestCase):

    def test_star_graph(self):
        edges = [
            (1, 2),
            (1, 3),
            (1, 4),
            (1, 5)
        ]
        graph = connected_component.edges_to_graph(edges)
        self.assertTrue(connected_component.is_connected(graph))

    def test_line_graph(self):
        edges = [
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5)
        ]
        graph = connected_component.edges_to_graph(edges)
        self.assertTrue(connected_component.is_connected(graph))

    def test_redundant_graph(self):
        edges = [
            (1, 2),
            (1, 2),
            (2, 1),
            (2, 1),
            (2, 1),
            (2, 1),
            (2, 3),
            (3, 4),
            (4, 5)
        ]
        graph = connected_component.edges_to_graph(edges)
        self.assertTrue(connected_component.is_connected(graph))

    def test_redundant_false_graph(self):
        edges = [
            (1, 2),
            (1, 2),
            (2, 1),
            (2, 1),
            (2, 1),
            (2, 1),
            (7, 8)
        ]
        graph = connected_component.edges_to_graph(edges)
        self.assertFalse(connected_component.is_connected(graph))

    def test_zero_based_graph(self):
        edges = [
            (0, 2),
            (1, 2),
            (2, 1),
            (2, 1),
            (2, 1),
            (2, 1),
            (0, 888)
        ]
        graph = connected_component.edges_to_graph(edges)
        self.assertTrue(connected_component.is_connected(graph))

    def test_large_graph(self):
        edges = [(random.randint(0, 10000), random.randint(0, 10000)) for k in range(100000)]
        graph = connected_component.edges_to_graph(edges)
        connected_component.is_connected(graph)
        self.assertTrue(True)


def main():
    unittest.main()

if __name__ == '__main__':
    main()
