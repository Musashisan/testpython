'''
Created on 30 mar. 2019

@author: musa
'''
from domain.position import Position
from builtins import int

class Screen(object):
    '''
    classdocs
    '''    
    img = None

    def __init__(self, position: Position, width: int, height: int):
        '''
        Constructor
        '''
        self.position = position
        self.width = width
        self.height = height
