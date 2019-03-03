'''
Created on 17 feb. 2019

@author: musa
'''
import cv2
import time
from grabscreen import grab_screen
#import pyautogui
import win32api, win32con


if __name__ == '__main__':
    last_time = time.time()
    frame = 0
    x = 0
    y = 0
    while True:
        frame += 1
        #Size 8, 32, 1142, 670
#        screen = grab_screen(region=(8, 32, 1142, 670))
        hwndChild, rect,screen = grab_screen("Clicker Heroes")
        print('Frame took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

        # new_screen, original_image, m1, m2 = process_img(screen)
        # cv2.imshow('window', new_screen)
        cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

        # action
        x = int(rect[2]*75/100)
        y = int(rect[3]/2)

        print(frame)
        if (frame % 40 == 0):
            print(x ,y)
            lParam = win32api.MAKELONG(x, y)
            #win32api.SendMessage(hwndChild, win32con.WM_MOUSEMOVE,0,lParam)
            win32api.SendMessage(hwndChild, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam)
            win32api.SendMessage(hwndChild, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, lParam)

            frame = 0

        
        # cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
