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

TEMPLATES = ["golden_treasure.jpg","treasure.jpg"]
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
            img = cv2.imread(file_path + '/'+template, 1)
            if (img is None):
                print("Template image '{}' notloaded".format(template))
            else:
                cv2.imshow("{0}".format(template),img)
                self.template_images.append(img)
        
    def get_status(self, screen: Screen) -> Village:
        village = Village()
    #    methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']    
        method = cv2.TM_CCOEFF
        for template in self.template_images:
            res = cv2.matchTemplate(screen.img,template,method)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            h, w, channels = template.shape
            bottom_right = (top_left[0] + w, top_left[1] + h)
            
            village.treasure = Treasure(TreasureType.ADVERTISE, Position(top_left[0], top_left[1]))
            print("treasure {0}".format(village.treasure))
#            cv2.rectangle(screen.img,top_left,bottom_right,255,2)
    
        return village
        