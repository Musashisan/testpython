'''
Created on 6 abr. 2019

@author: musa
'''

from enum import Enum

class GameState(Enum):

    VILLAGE = 1,
    
    ADVERTISE = 2,
    
    PROMPT_ADVERTISE = 3,
    
    UNKNOWN = 99,
    
    TEST = 100