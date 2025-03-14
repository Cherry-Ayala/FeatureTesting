# test_shortestPath.py
# Instructions: To run these tests, ensure you have Python installed. This script uses the unittest library, which comes with Python by default.
# To run the tests, simply execute the command: python -m unittest test_shortestPath.py

import unittest
from src.DemoFrida import shortestPath

class TestShortestPath(unittest.TestCase):

    # Happy Paths
    def test_simple_path(self):
        """Test the normal case with a simple path from start to end"""
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'C': 2, 'D': 5},
            'C': {'D': 1},
            'D': {}
        }
        self.assertEqual(shortestPath(graph, 'A', 'D'), ['A', 'B', 'C', 'D'])

    def test_no_path(self):
        """Test case where no path exists between start and end nodes"""
        graph = {
            'A': {'B': 1},
            'B': {'C': 2},
            'C': {},
            'D': {}
        }
        self.assertIsNone(shortestPath(graph, 'A', 'D'))

    def test_direct_path(self):
        """Test case with direct path from start to end without intermediate nodes"""
        graph = {
            'A': {'B': 1},
            'B': {},
            'C': {},
        }
        self.assertEqual(shortestPath(graph, 'A', 'B'), ['A', 'B'])

    # Edge Cases
    def test_empty_graph(self):
        """Test case with an empty graph"""
        graph = {}
        self.assertIsNone(shortestPath(graph, 'A', 'B'))

    def test_same_node(self):
        """Test case where start and end nodes are the same"""
        graph = {
            'A': {'B': 1},
            'B': {'A': 1}
        }
        self.assertEqual(shortestPath(graph, 'A', 'A'), ['A'])

    def test_negative_weights(self):
        """Test case with negative weight cycles (should return None if not handled)"""
        graph = {
            'A': {'B': -1},
            'B': {'A': -1}
        }
        self.assertIsNone(shortestPath(graph, 'A', 'B'))

    def test_nonexistent_node(self):
        """Test case with a start or end node that does not exist in the graph"""
        graph = {
            'A': {'B': 1},
            'B': {'C': 2},
            'C': {}
        }
        self.assertIsNone(shortestPath(graph, 'A', 'D'))