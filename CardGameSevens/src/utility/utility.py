'''
Created on 13 Jun 2020

@author: Chris
'''


def contains(obj_list, filter_fcn):
    '''
    Method for returning an obj
    from a list of objs based on filter input.
    '''

    for obj in obj_list:
        if filter_fcn(obj):
            return True
    return False


def pad(lst, content, width):
    '''Pads a list of strings with empty strings until specified index'''

    return lst.extend([content] * (width - len(lst)))
