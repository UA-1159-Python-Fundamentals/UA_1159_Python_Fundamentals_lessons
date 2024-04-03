import unittest
from hw.hw14.ohotass.functions import greeting_by_name, get_symbol_position, merge
from hw.hw14.ohotass.functions_with_errors import greeting_by_name as greeting_by_name_err, \
    get_symbol_position as get_symbol_position_err, merge as merge_err


class TestFunctions(unittest.TestCase):
    def test_greeting_by_name(self):
        self.assertEqual(greeting_by_name("Alice"), "Hello Alice!")
        self.assertEqual(greeting_by_name("Bob"), "Hello Bob!")

    def test_get_symbol_position(self):
        self.assertEqual(get_symbol_position("hello", "l"), 3)
        self.assertEqual(get_symbol_position("world", "o"), 5)
        self.assertEqual(get_symbol_position("hello", "z"), -1)

    def test_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        merged_dict = merge(dict1.copy(), dict2.copy())
        self.assertEqual(merged_dict, {'a': 1, 'b': 2, 'c': 3, 'd': 4})
        # Check immutability of dict1 and dict2
        self.assertEqual(dict1, {'a': 1, 'b': 2})
        self.assertEqual(dict2, {'c': 3, 'd': 4})


class TestFunctionsWithErrors(unittest.TestCase):
    def test_greeting_by_name(self):
        self.assertEqual(greeting_by_name_err("Alice"), "Hello name!")

    def test_get_symbol_position(self):
        self.assertEqual(get_symbol_position_err("hello", "l"), 3)
        self.assertEqual(get_symbol_position_err("world", "o"), 5)
        self.assertEqual(get_symbol_position_err("hello", "z"), -1)

    def test_merge(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'c': 3, 'd': 4}
        merged_dict = merge_err(dict1.copy(), dict2.copy())
        self.assertEqual(merged_dict, {'a': 1, 'b': 2, 'c': 3, 'd': 4})
        # Check immutability of dict1 and dict2
        self.assertEqual(dict1, {'a': 1, 'b': 2})  # This will fail as the dict1 is mutated
        self.assertEqual(dict2, {'c': 3, 'd': 4})  # This will fail as the dict2 is mutated


if __name__ == '__main__':
    unittest.main()
