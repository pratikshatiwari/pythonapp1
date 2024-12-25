import unittest
import tempfile
import os
from app import count_lines, contains_keyword

    # Unused variables
    
unused_var_1 = 100  # Declared but never used
unused_var_2 = "This is not used"  # Declared but never used
unused_var_3 = [1, 2, 3]  # Declared but never used

class TestAppFunctions(unittest.TestCase):
    
    def setUp(self):
        """
        Set up a temporary file for testing.
        """
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.write(b"Hello World\nThis is a test file\nAnother line with keyword\n")
        self.test_file.close()

    def tearDown(self):
        """
        Clean up the temporary file after tests.
        """
        os.unlink(self.test_file.name)

    def test_count_lines(self):
        """
        Test the count_lines function.
        """
        result = count_lines(self.test_file.name)
        self.assertEqual(result, 3)

    def test_contains_keyword_found(self):
        """
        Test the contains_keyword function when the keyword is present.
        """
        result = contains_keyword(self.test_file.name, "keyword")
        self.assertTrue(result)

    def test_contains_keyword_not_found(self):
        """
        Test the contains_keyword function when the keyword is not present.
        """
        result = contains_keyword(self.test_file.name, "missing")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
