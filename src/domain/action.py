'''
Created on 16 mar. 2019

@author: Musa
'''

class Action(object):
    '''
    classdocs
    '''


    def __init__(self, next_state = None):
        '''
        Constructor
        '''       
        self.next_state = next_state
        
    def execute(self):
        return self.next_state