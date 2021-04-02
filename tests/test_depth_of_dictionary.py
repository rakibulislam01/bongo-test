import unittest
import depth_of_dictionary


class TestDepthOfDictionary(unittest.TestCase):

    def setUp(self) -> None:
        self.a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }

    def test_dictionary(self):
        self.assertEqual(depth_of_dictionary.dict_depth(self.a), ['key1 1', 'key2 1', 'key3 2', 'key4 2', 'key5 3'])

    def test_empty_dict(self):
        self.assertEqual(depth_of_dictionary.dict_depth({}), [])

    def test_data_type(self):
        self.assertEqual(depth_of_dictionary.dict_depth([]), [])


if __name__ == '__main__':
    unittest.main()
