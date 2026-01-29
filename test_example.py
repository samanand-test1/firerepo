"""
Example test file for the firerepo repository.
This file demonstrates basic unit testing structure.
"""

import unittest


class TestExample(unittest.TestCase):
    """Example test class to demonstrate test structure."""

    def test_addition(self):
        """Test basic addition."""
        self.assertEqual(1 + 1, 2)

    def test_string_concatenation(self):
        """Test string concatenation."""
        result = "Hello" + " " + "World"
        self.assertEqual(result, "Hello World")

    def test_list_operations(self):
        """Test list operations."""
        test_list = [1, 2, 3]
        test_list.append(4)
        self.assertEqual(len(test_list), 4)
        self.assertIn(2, test_list)


if __name__ == '__main__':
    unittest.main()
