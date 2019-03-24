'''
Created on 17 feb. 2019

@author: musa

'''
import cv2
import time
from grabscreen import grab_screen,find_dialog_wildcard
import input
import win32api, win32con
import sys
import numpy as np

#WINDOW_NAME = "Clicker Heroes"
WINDOW_NAME = "NoxPlayer"
TEMPLATES = ["collect.jpg","golden_treasure.jpg","treasure.jpg"]
#TEMPLATES = ["collect.jgp","golden_treasure.jpg","treasure.jpg"]

def load_templates(image_file_array):
    search_images = []
    for template in image_file_array:
        img = cv2.imread(template, 1)
        if (img is None):
            print("Template image '{}' notloaded".format(template))
        else:
            cv2.imshow("{0}".format(template),img)
            search_images.append(img)
    
    return search_images

def process_img(screen,template_images):
#    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']    
    method = cv2.TM_CCOEFF
    for template in template_images:
        res = cv2.matchTemplate(screen,template,method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc
        h, w, channels = template.shape
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(screen,top_left,bottom_right,255,2)

    return screen

if __name__ == '__main__':
#    find_dialog_wildcard("^[Nn].*")
    template_images = load_templates(TEMPLATES)
    last_time = time.time()
    frame = 0
    x = 0
    y = 0
    while True:
        frame += 1
        #Size 8, 32, 1142, 670
#        screen = grab_screen(region=(8, 32, 1142, 670))
        hwndChild, rect, screen = grab_screen(WINDOW_NAME)
        print('Frame took {} seconds'.format(time.time() - last_time))
        last_time = time.time()

        # new_screen, original_image, m1, m2 = process_img(screen)
        # cv2.imshow('window', new_screen)
        screen = process_img(screen, template_images)
        cv2.imshow('window2', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

        # action
        x = int(rect[2]*75/100)
        y = int(rect[3]/2)

        print(frame)
        if (frame % 40 == 0):
            print(x ,y)
#            input.left_click(hwndChild, x, y)

            frame = 0

        
        # cv2.imshow('window',cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
