'''
Created on 6 abr. 2019

@author: musa
'''
from enum import Enum, IntFlag
from domain.key_enum import KeyEnum

class EnumTest(IntFlag):
    LA = 0,
    LO = 1

if __name__ == '__main__':
    la = KeyEnum.ESC
    
    print(la)
    print(la.value)
    print(la.name)
    
    foo = EnumTest.LA
    
    print(foo)
    print(foo.name)
    print(foo.value)