'''
Created on 17 feb. 2019

@author: musa

'''
import time

from infrastructure.services.app_service_impl import AppServiceImpl
from infrastructure.services.village_service_impl import VillageServiceImpl
from api.window_server import WindowServer
from api.window_action import WindowAction
from infrastructure.screen_cv2_impl import ScreenCv2Impl 
from domain.position import Position
from domain.treaseure_type import TreasureType

WINDOW_NAME = "CrushTemAllBot"
APPLICATION_NAME = "NoxPlayer"

if __name__ == '__main__':
    server = WindowServer(WINDOW_NAME)
    village_service = VillageServiceImpl()
    screen = ScreenCv2Impl()
        
    application = AppServiceImpl(APPLICATION_NAME)
    application.start()
    last_time = time.time()
    while True:
        
        screen = application.update_screen(screen)
        
        village = village_service.get_status(screen)
        treasure = village.treasure
        # 541 990
        #cv2.rectangle(screen.img,(0,y),(541,y2),255,2)
        if (treasure):
            if (treasure.type == TreasureType.SIMPLE):
                application.left_click(treasure.position)
                #screen.paint_rectangle(treasure.position, treasure.position.add(Position(20,20)))
              
        server.show_screen(screen)
#        print('Frame took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        
        action = server.get_action()
#            input.left_click(hwndChild, x, y)

        if (action == WindowAction.EXIT):
            server.close()
            break
