'''
Created on 30 mar. 2019

@author: musa
'''
from domain.services.app_service import AppService
from domain.screen import Screen

import cv2
import numpy as np
import win32gui, win32ui, win32con,win32api
import re

from domain.position import Position
from builtins import int
from domain.ioc import RequiredFeature, IsInstanceOf
import time

class AppServiceImpl(AppService):
    '''
    classdocs
    '''
    
    def __init__(self, window_name: str):
        '''
        Constructor
        '''
        super().__init__(window_name)
        self._handler = None
        self.left = None
        self.top = None
        self.width = None
        self.height = None
        self._img = None
        
    def start(self):
        self._handler = win32gui.FindWindow(None, self._window_name)
        rect = win32gui.GetWindowRect(self._handler)
        self.left = rect[0]
        self.top = rect[1]
        self.width = rect[2] - self.left
        self.height = rect[3] - self.top

    def _update_screen(self):
        self.handlerdc = win32gui.GetWindowDC(self._handler)
        srcdc = win32ui.CreateDCFromHandle(self.handlerdc)
        memdc = srcdc.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, self.width, self.height)
        memdc.SelectObject(bmp)
        memdc.BitBlt((0, 0), (self.width, self.height), srcdc, (0, 0), win32con.SRCCOPY)
        
        signedIntsArray = bmp.GetBitmapBits(True)
        self._img = np.fromstring(signedIntsArray, dtype='uint8')
        self._img.shape = (self.height,self.width,4)
    
        srcdc.DeleteDC()
        memdc.DeleteDC()
        win32gui.ReleaseDC(self._handler, self.handlerdc)
        win32gui.DeleteObject(bmp.GetHandle())

    def update_screen(self, screen: Screen) -> Screen:
        self._update_screen()
        screen.configure(Position(self.left, self.top), self.width, self.height)
        #screen.img = cv2.cvtColor(self._img, cv2.COLOR_BGRA2RGB)
        screen.img = cv2.cvtColor(self._img, cv2.COLOR_BGR2GRAY)
        
        return screen

    def left_click(self, position: Position) -> None:
#        win32gui.SetActiveWindow(self._handler)
        lParam = win32api.MAKELONG(position.x, position.y)
        win32api.SendMessage(self._handler, win32con.WM_MOUSEMOVE,0,lParam)
        time.sleep(0.2)
        win32api.SendMessage(self._handler, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        time.sleep(0.1)
        win32api.SendMessage(self._handler, win32con.WM_LBUTTONUP, 0, lParam)

    def _find_dialog_wildcard(self,window_name_regexp):
        ''' Enumerate all the dialog to find the dialog which title matches the title'''              
        def callback(hwnd, window_name_regexp):
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                if (re.search(window_name_regexp, title)):
                    print(title)
            return True
        win32gui.EnumWindows(callback, window_name_regexp)