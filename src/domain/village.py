'''
Created on 31 mar. 2019

@author: musa
'''
from domain.treasure import Treasure
from domain.position import Position

class Village(object):

    treasure: Treasure = None
    
    collect: Position = None
    
    upgrade: Position = None
    
    prompt_advertise: bool = False

