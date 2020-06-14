'''
Created on 13 Jun 2020

@author: Chris
'''

def contains(obj_list, filter):
    '''Method for returning an obj from a list of objs based on filter input.'''

    for x in obj_list:
        if filter(x):
            return True
    return False

def pad(l, content, width):
    '''Pads a list of strings with empty strings until specified index'''

    l.extend([content] * (width - len(l)))
    return l
