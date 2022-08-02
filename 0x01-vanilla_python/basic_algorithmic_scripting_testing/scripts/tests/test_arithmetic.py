"""
Parts or Components of Test
- System under test (function, class, method)
- Test case class (unittest.TestCase)
- Assertions
- Test suite
- Test runnner (unittest, pytest, nose)
"""
import unittest

from arithmetic import add


class TestAdd(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add(10, 30), 40, "The result should be 40")
    
    def test_add_numbers_with_wrong_data(self):
        with self.assertRaises(TypeError):
            result = add(10, "fifty")


if __name__ == "__main__":
    unittest.main(verbosity=2)
