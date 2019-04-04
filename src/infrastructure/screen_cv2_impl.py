'''
Created on 4 abr. 2019

@author: musa
'''

import cv2
from domain.screen import Screen
from domain.position import Position

class ScreenCv2Impl(Screen):
    
    def __init__(self):
        super().__init__()
         
    def paint_rectangle(self, top_left: Position, bottom_right: Position) -> None:
        cv2.rectangle(self.img,top_left.tuple(),bottom_right.tuple(),255,2)