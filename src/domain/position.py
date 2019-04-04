'''
Created on 29 mar. 2019

@author: musa
'''
from typing import Tuple
from builtins import str

class Position(object):
    '''
    classdocs
    '''

    def __init__(self, x, y):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        
    def __str__(self) -> str:
        return "x = {0}, y = {1}".format(self.x, self.y)
    
    def add(self, position):
        return Position(self.x + position.x, self.y + position.y)
    
    def tuple(self) -> Tuple:
        return (self.x, self.y)

