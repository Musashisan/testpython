'''
Created on 29 mar. 2019

@author: musa
'''
from abc import ABC, abstractmethod

from domain.village import Village
from domain.screen import Screen

class VillageService(ABC):
        
    @abstractmethod
    def get_status(self, screen: Screen) -> Village:
        pass
    
    

