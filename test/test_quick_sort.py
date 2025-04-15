# test_quick_sort.py
# Instructions:
# 1. Ensure Python is installed on your system.
# 2. Save this file as test_quick_sort.py.
# 3. Install the `unittest` library, if not already installed (it is part of the standard library).
# 4. Run the tests using the command: python -m unittest test_quick_sort.py

import unittest
from src.test2 import quickSort

# Happy Paths
class TestQuickSort(unittest.TestCase):
    """Unit test class for quickSort function."""

    def test_sorted_array(self):
        """Test quickSort with an already sorted array."""
        self.assertEqual(quickSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        """Test quickSort with a reverse sorted array."""
        self.assertEqual(quickSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_random_unsorted_array(self):
        """Test quickSort with a random unsorted array."""
        self.assertEqual(quickSort([3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])

    def test_array_with_duplicates(self):
        """Test quickSort with an array containing duplicates."""
        self.assertEqual(quickSort([3, 1, 4, 4, 5, 2, 1]), [1, 1, 2, 3, 4, 4, 5])

    def test_single_element_array(self):
        """Test quickSort with a single element array."""
        self.assertEqual(quickSort([1]), [1])

    def test_empty_array(self):
        """Test quickSort with an empty array."""
        self.assertEqual(quickSort([]), [])

# Edge Cases
    def test_array_with_negative_numbers(self):
        """Test quickSort with an array containing negative numbers."""
        self.assertEqual(quickSort([-1, -3, -2, 0, 2, 1]), [-3, -2, -1, 0, 1, 2])

    def test_array_with_zeros(self):
        """Test quickSort with an array containing zeros."""
        self.assertEqual(quickSort([0, 0, 0, 0, 0]), [0, 0, 0, 0, 0])

    def test_array_with_large_numbers(self):
        """Test quickSort with an array containing large numbers."""
        self.assertEqual(quickSort([1000000, 999999, 1000001]), [999999, 1000000, 1000001])

    def test_non_numeric_input(self):
        """Test quickSort with non-numeric input to ensure type error handling."""
        with self.assertRaises(TypeError):
            quickSort(['a', 'b', 'c'])

if __name__ == "__main__":
    unittest.main()