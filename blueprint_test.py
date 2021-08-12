import unittest
from blueprint import api_call


# Since the only independent variable in this use case is the address input as a string,
# only unit test required is for the API call to see if the given string can be matched with any location.
class TestBlueprint(unittest.TestCase):
    def test_api_call(self):
        with self.assertRaises(ValueError):
            api_call("aaabbbccc")
            api_call("3142556")
            api_call("__??..**")
