'''
Created on 17 feb. 2019

@author: musa
'''
# Done by Frannecklp

import cv2
import numpy as np
import win32gui, win32ui, win32con

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