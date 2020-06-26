'''
Created on 13 Jun 2020

@author: Chris
'''


def pad(lst, content, width):
    '''Pads a list of strings with empty strings until specified index'''

    return lst.extend([content] * (width - len(lst)))
