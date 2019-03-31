'''
Created on 30 mar. 2019

@author: musa
'''
from abc import ABC, abstractmethod
from domain.screen import Screen
from domain.position import Position

class AppService(ABC):
    '''
    classdocs
    '''


    def __init__(self, window_name: str):
        '''
        Constructor
        '''
        self._window_name = window_name
        
    @property
    def window_name(self) -> str:
        return self._window_name
        
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def grab_screen(self) -> Screen:
        pass

    @abstractmethod
    def left_click(self, position: Position) -> None:
        pass
