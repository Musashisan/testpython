'''
Created on 30 mar. 2019

@author: musa
'''
from abc import ABC, abstractmethod
from domain.screen import Screen
from domain.position import Position
from domain.key_enum import KeyEnum

class AppService(ABC):
    '''
    classdocs
    '''


    def __init__(self, window_name: str, widget_name = ""):
        '''
        Constructor
        '''
        self._window_name = window_name
        self._widget_name = widget_name

        
    @property
    def window_name(self) -> str:
        return self._window_name
        
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def update_screen(self, screen: Screen) -> Screen:
        pass

    @abstractmethod
    def left_click(self, position: Position) -> None:
        pass

    @abstractmethod
    def press_key(self, *args: KeyEnum) -> None:
        pass