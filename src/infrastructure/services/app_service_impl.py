'''
Created on 30 mar. 2019

@author: musa
'''
from domain.services.app_service import AppService
from domain.screen import Screen

import cv2
import numpy as np
import win32gui, win32ui, win32con, win32api
import re

from domain.position import Position
import time
from domain.key_enum import KeyEnum


class AppServiceImpl(AppService):
    '''
    classdocs
    '''
        
    def __init__(self, window_name: str, widget_name = ""):
        '''
        Constructor
        '''
        super().__init__(window_name, widget_name)
        self._handler = None
        self. _handler_widget = None
        self.left = None
        self.top = None
        self.width = None
        self.height = None
        self._img = None
        self._childs = {}

    def winfun(self, hwnd, lparam):
        s = win32gui.GetWindowText(hwnd)
        if len(s) > 0:
            print("winfun, child_hwnd: %d   txt: %s" % (hwnd, s))
            rect = win32gui.GetWindowRect(hwnd)
            self._childs[s] = hwnd
            print(rect)
        return 1
        
    def start(self):
        self._handler = win32gui.FindWindow(None, self._window_name)
        rect = win32gui.GetWindowRect(self._handler)
        self.left = rect[0]
        self.top = rect[1]
        self.width = rect[2] - self.left
        self.height = rect[3] - self.top
        win32gui.EnumChildWindows(self._handler, self.winfun, None)
        self._handler_widget = self._childs.get(self._widget_name, self._handler)

    def _update_screen(self):
        self.handlerdc = win32gui.GetWindowDC(self._childs["centralWidgetWindow"])
        srcdc = win32ui.CreateDCFromHandle(self.handlerdc)
        memdc = srcdc.CreateCompatibleDC()
        bmp = win32ui.CreateBitmap()
        bmp.CreateCompatibleBitmap(srcdc, self.width, self.height)
        memdc.SelectObject(bmp)
        memdc.BitBlt((0, 0), (self.width, self.height), srcdc, (0, 0), win32con.SRCCOPY)
        
        signedIntsArray = bmp.GetBitmapBits(True)
        self._img = np.fromstring(signedIntsArray, dtype='uint8')
        self._img.shape = (self.height, self.width, 4)
    
        srcdc.DeleteDC()
        memdc.DeleteDC()
        win32gui.ReleaseDC(self._handler, self.handlerdc)
        win32gui.DeleteObject(bmp.GetHandle())

    def update_screen(self, screen: Screen) -> Screen:
        self._update_screen()
        screen.configure(Position(self.left, self.top), self.width, self.height)
        # screen.img = cv2.cvtColor(self._img, cv2.COLOR_BGRA2RGB)
        screen.img = cv2.cvtColor(self._img, cv2.COLOR_BGR2GRAY)
        
        return screen

    def left_click(self, position: Position) -> None:
        lParam = win32api.MAKELONG(position.x, position.y)
        win32api.SendMessage(self._handler, win32con.WM_MOUSEMOVE, 0, lParam)
        time.sleep(0.2)
        win32api.SendMessage(self._handler, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
        time.sleep(0.1)
        win32api.SendMessage(self._handler, win32con.WM_LBUTTONUP, 0, lParam)

    def press_key(self, *args: KeyEnum) -> None:
        '''
        one press, one release.
        accepts as many arguments as you want. e.g. press('left_arrow', 'a','b').
        '''
        for i in args:
#            win32api.SendMessage(self._handler, win32con.WM_CHAR, i.value, 0)
            win32api.SendMessage(self._handler_widget, win32con.WM_KEYDOWN, i.value, 0)
 #           win32api.keybd_event(i.value, 0, 0, 0)
            time.sleep(.05)
            win32api.SendMessage(self._handler_widget, win32con.WM_KEYUP, i.value, 0)            
#            win32api.keybd_event(i.value, 0 , win32con.KEYEVENTF_KEYUP , 0)

    def _find_dialog_wildcard(self, window_name_regexp):
        ''' Enumerate all the dialog to find the dialog which title matches the title'''              

        def callback(hwnd, window_name_regexp):
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                if (re.search(window_name_regexp, title)):
                    print(title)
            return True

        win32gui.EnumWindows(callback, window_name_regexp)
        
