'''
Created on 31 mar. 2019

@author: musa
'''
import cv2
from domain.screen import Screen
from builtins import str

from api.window_action import WindowAction


class WindowServer(object):
    '''
    classdocs
    '''


    def __init__(self, window_name: str):
        '''
        Constructor
        '''
        self._window_name = window_name
        
    def show_screen(self, screen: Screen) -> None:
        cv2.imshow(self._window_name, cv2.cvtColor(screen.img, cv2.COLOR_BGR2RGB))
        
    def get_action(self) -> WindowAction:
        
        if cv2.waitKey(25) & 0xFF == ord('q'):
            return WindowAction.EXIT
        
        return WindowAction.NONE
    
    def close(self) -> None:
        cv2.destroyAllWindows()
