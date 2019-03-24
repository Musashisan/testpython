'''
Created on 17 feb. 2019

@author: musa
'''
# Done by Frannecklp

import cv2
import numpy as np
import win32gui, win32ui, win32con
import re

def find_dialog_wildcard(window_name_regexp):
        ''' Enumerate all the dialog to find the dialog which title matches the title'''              
        def callback(hwnd, window_name_regexp):
            if win32gui.IsWindowVisible(hwnd):
                title = win32gui.GetWindowText(hwnd)
                if (re.search(window_name_regexp, title)):
                    print(title)
            return True
        win32gui.EnumWindows(callback, window_name_regexp)

        

def grab_screen(window_name):

    hwin = win32gui.FindWindow(None, window_name)
    rect = win32gui.GetWindowRect(hwin)
    left = rect[0]
    top = rect[1]
    width = rect[2] - left
    height = rect[3] - top
    
    hwindc = win32gui.GetWindowDC(hwin)
    srcdc = win32ui.CreateDCFromHandle(hwindc)
    memdc = srcdc.CreateCompatibleDC()
    bmp = win32ui.CreateBitmap()
    bmp.CreateCompatibleBitmap(srcdc, width, height)
    memdc.SelectObject(bmp)
    memdc.BitBlt((0, 0), (width, height), srcdc, (0, 0), win32con.SRCCOPY)
    
    signedIntsArray = bmp.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (height,width,4)

    srcdc.DeleteDC()
    memdc.DeleteDC()
    win32gui.ReleaseDC(hwin, hwindc)
    win32gui.DeleteObject(bmp.GetHandle())

    return hwin,(left, top, width, height),cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)