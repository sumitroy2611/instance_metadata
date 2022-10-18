import src
from src.get_meta_key import *
import unittest

# ========================================================================================================
# This is the unit test class to validate the functionality for get meta key value
# ========================================================================================================
class Testing(unittest.TestCase):

    # test case function to check field value returned as per meta key
    def test_meta_key(self):
        search_object = 'ami-id'

        expected_result = 'ami-'

        result = search(str(search_object))
        self.assertIn(expected_result,result)

        print("Start field is %s and result is %s\n" %(search_object,expected_result))

if __name__ == '__main__':
        # begin the unittest.main()
        unittest.main()
