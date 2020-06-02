#!/usr/bin/python3
def lookup(obj):
    '''function that returns the list of available
    attributes and methods of an object'''
    lk_list = dir(obj)
    return lk_list
