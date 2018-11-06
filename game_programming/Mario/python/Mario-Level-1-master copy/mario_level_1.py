#!/usr/bin/env python
__author__ = 'justinarmstrong'

"""
This is an attempt to recreate the first level of
Super Mario Bros for the NES.
"""

import sys
import pygame as pg
from data.main import main
import cProfile
from inspect import currentframe, getframeinfo

cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

if __name__=='__main__':
    main()
    pg.quit()
    sys.exit()