
import win32api,win32con

def left_click(hwndChild, x, y):
    lParam = win32api.MAKELONG(x, y)
    #win32api.SendMessage(hwndChild, win32con.WM_MOUSEMOVE,0,lParam)
    win32api.SendMessage(hwndChild, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
    win32api.SendMessage(hwndChild, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)
