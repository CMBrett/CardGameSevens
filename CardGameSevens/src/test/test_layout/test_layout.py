'''
Created on 11 Jun 2020

@author: Chris
'''
import unittest
from layout.layout import Layouts

class TestLayouts(unittest.TestCase):
    '''
    '''

    def test_layouts(self):
        '''
        '''
        test_layouts = Layouts(2)
        self.assertEqual(len(test_layouts.layouts), 8)
        print(test_layouts.layouts)
        
        for layout in test_layouts.layouts:
            print((layout.suit, layout.layout_num))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testLayout']
    unittest.main()