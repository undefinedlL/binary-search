import unittest
from main import binary_search

def _test(target_value, value_index_result, self):
        arr = [1, 3, 4, 6, 7, 8, 15, 56]
        result = binary_search(arr, target_value, 0, len(arr) - 1)
        self.assertEqual(result, value_index_result)

class TestCase(unittest.TestCase):
    
    def test_binary_search1(self):
        _test(1, 0, self)
        
    def test_binary_search2(self):
        _test(3, 1, self)
        
    def test_binary_search3(self):
        _test(4, 2, self)

    def test_binary_search4(self):
        _test(6, 3, self)
        
    def test_binary_search5(self):
        _test(7, 4, self)
        
    def test_binary_search6(self):
        _test(8, 5, self)
    
    def test_binary_search7(self):
        _test(15, 6, self)  
    
    def test_binary_search8(self):
        _test(56, 7, self)
    
    def test_binary_search9(self):
        _test(123134, None, self)
        
    
if __name__ == '__main__':
    unittest.main()