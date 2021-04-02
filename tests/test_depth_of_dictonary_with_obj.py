import unittest
import depth_of_dictionary_with_obj


class TestDepthOfDictionaryObj(unittest.TestCase):

    def setUp(self) -> None:
        self.person_a = depth_of_dictionary_with_obj.Person('user', 1, None)
        self.a = {
            "key1": 1,
            "key2": self.person_a
        }

    def test_dictionary(self):
        self.assertEqual(depth_of_dictionary_with_obj.dict_depth(self.a), ['key1 1', 'key2 1', 'first_name 2', 'last_name 2', 'father 2'])

    def test_empty_dict(self):
        self.assertEqual(depth_of_dictionary_with_obj.dict_depth({}), [])

    def test_data_type(self):
        self.assertEqual(depth_of_dictionary_with_obj.dict_depth([]), [])


if __name__ == '__main__':
    unittest.main()
