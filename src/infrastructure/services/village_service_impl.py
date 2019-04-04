'''
Created on 29 mar. 2019

@author: musa
'''
import cv2
import os
from domain.position import Position
from domain.services.village_service import VillageService
from domain.screen import Screen
from domain.village import Village
from domain.treasure import Treasure
from domain.treaseure_type import TreasureType
from matplotlib import pyplot as plt

TEMPLATES = [{"name":"treasure","file":"treasure.jpg"},{"name":"golden","file":"golden_treasure.jpg"}]
#TEMPLATES = ["collect.jpg","golden_treasure.jpg","treasure.jpg"]

class VillageServiceImpl(VillageService):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.template_images = []
        self._load_templates()

    def _load_templates(self):
        file_path = os.path.dirname(os.path.abspath(__file__))
        for template in TEMPLATES:
            img = cv2.imread(file_path + '/'+template["file"], cv2.IMREAD_GRAYSCALE)
            #img = cv2.imread(file_path + '/'+template, cv2.IMREAD_COLOR)
            print(cv2.IMREAD_COLOR)
            if (img is None):
                print("Template image '{}' notloaded".format(template))
            else:
                #cv2.imshow("{0}".format(template),img)
                self.template_images.append({"name":template["name"],"image":img})
        
    def get_status(self, screen: Screen) -> Village:
        village = Village()
    #    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']    
        method = cv2.TM_CCOEFF
        for template in self.template_images:
            res = cv2.matchTemplate(screen.img[int(screen.height/10):int(4*screen.height/10), 0:screen.width],template["image"],method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = (max_loc[0], max_loc[1]+int(screen.height/10))
            #h, w, channels = template.shape
            h, w = template["image"].shape
            bottom_right = (top_left[0] + w, top_left[1] + h)
            if template["name"] == "treasure" and max_val > 1300000:
                print(max_val)
                cv2.rectangle(screen.img,top_left, bottom_right, 255, 2)
                village.treasure = Treasure(TreasureType.SIMPLE, Position(top_left[0]+int(w/2), top_left[1]+int(h/2)))
                print("treasure '{0}'".format(village.treasure.position))
            elif template["name"] == "golden" and max_val > 3420000:
                print(max_val)
                village.treasure = Treasure(TreasureType.ADVERTISE, Position(top_left[0]+int(w/2), top_left[1]+int(h/2)))
                cv2.rectangle(screen.img,top_left, bottom_right, 255, 2)
                print("golden '{0}'".format(village.treasure.position))

            #plt.subplot(121),plt.imshow(res,cmap = 'gray')
            #plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
            #plt.subplot(122),plt.imshow(screen.img,cmap = 'gray')
            #plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
            #plt.suptitle('TM_CCOEFF')
            #plt.show()
                
        return village
        