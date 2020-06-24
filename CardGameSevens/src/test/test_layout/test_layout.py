'''
Created on 11 Jun 2020

@author: Christopher Brett
'''
import unittest
from layout.layout import Layouts


class TestLayouts(unittest.TestCase):
    '''
    This test class tests the functionality within
    the layout.layout module.
    '''

    def test_layouts(self):
        '''
        This test ensures that the correct number
        of layouts are created per deck.
        '''

        test_layouts = Layouts(2)
        self.assertEqual(len(test_layouts.layouts), 8)


if __name__ == "__main__":
    unittest.main()
