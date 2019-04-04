'''
Created on 31 mar. 2019

@author: musa
'''
from domain.treaseure_type import TreasureType
from domain.position import Position

class Treasure(object):
    '''
    classdocs
    '''
    position: Position = None
    type: TreasureType = None

    def __init__(self, treasure_type: TreasureType, position = Position):
        '''
        Constructor
        '''
        self.position = position
        self.type = treasure_type