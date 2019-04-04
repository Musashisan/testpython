'''
Created on 30 mar. 2019

@author: musa
'''

from abc import ABC, abstractmethod
from domain.position import Position
from builtins import int

class Screen(ABC):
    '''
    classdocs
    '''    
    img = None
    position: Position
    width: int
    height: int

    def __init__(self):
        '''
        Constructor
        '''
        
    def configure(self, position: Position, width: int, height: int):
        self.position = position
        self.width = width
        self.height = height
        
    @abstractmethod
    def paint_rectangle(self, top_left: Position, bottom_right: Position) -> None:
        pass