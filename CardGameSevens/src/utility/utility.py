'''
Created on 13 Jun 2020

@author: Chris
'''

def contains(obj_list, filter):
    '''
    '''
    for x in obj_list:
        if filter(x):
            return True
    return False

def pad(l, content, width):
    '''
    '''
    l.extend([content] * (width - len(l)))
    return l