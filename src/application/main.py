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
from domain.game_state import GameState
from domain.key_enum import KeyEnum

WINDOW_NAME = "CrushTemAllBot"
APPLICATION_NAME = "NoxPlayer"
APPLICATION_WIDGET = "centralWidgetWindow"

if __name__ == '__main__':
    server = WindowServer(WINDOW_NAME)
    village_service = VillageServiceImpl()
    screen = ScreenCv2Impl()
        
    application = AppServiceImpl(APPLICATION_NAME, APPLICATION_WIDGET)
    application.start()
    last_time = time.time()
    state = GameState.VILLAGE
    while True:
        
        if state == GameState.TEST:
            application.press_key(KeyEnum.ESC)
        
        screen = application.update_screen(screen)
        if state == GameState.VILLAGE:
            village = village_service.get_status(screen)
            treasure = village.treasure
            
            if (treasure):
                if (treasure.type == TreasureType.SIMPLE):
                    application.left_click(treasure.position)
                    #screen.paint_rectangle(treasure.position, treasure.position.add(Position(20,20)))
                elif (treasure.type == TreasureType.ADVERTISE):
                    application.left_click(treasure.position)
#                    state = GameState.ADVERTISE
                    
            if (village.prompt_advertise):
                state = GameState.PROMPT_ADVERTISE
                print("prompt advertise!!")
        elif state == GameState.PROMPT_ADVERTISE:
                application.press_key(KeyEnum.ESC)
                state = GameState.VILLAGE

        elif state == GameState.ADVERTISE:
            time.sleep(30)
            application.press_key(KeyEnum.ESC)
            state = GameState.VILLAGE
                
              
        server.show_screen(screen)
#        print('Frame took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        
        action = server.get_action()
#            input.left_click(hwndChild, x, y)

        if (action == WindowAction.EXIT):
            server.close()
            break
