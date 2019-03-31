'''
Created on 17 feb. 2019

@author: musa

'''
import time

from infrastructure.services.app_service_impl import AppServiceImpl
from infrastructure.services.village_service_impl import VillageServiceImpl
from api.window_server import WindowServer
from api.window_action import WindowAction

WINDOW_NAME = "CrushTemAllBot"
APPLICATION_NAME = "NoxPlayer"

if __name__ == '__main__':
    server = WindowServer(WINDOW_NAME)
    village_service = VillageServiceImpl()
    
    application = AppServiceImpl(APPLICATION_NAME)
    application.start()
    last_time = time.time()
    while True:
        
        screen = application.grab_screen()
        server.show_screen(screen)
        
        village = village_service.get_status(screen)
                  
        if (village.treasure):
            print("Treasure found !!!")
              
#        print('Frame took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        
        action = server.get_action()
#            input.left_click(hwndChild, x, y)

        if (action == WindowAction.EXIT):
            server.close()
            break
