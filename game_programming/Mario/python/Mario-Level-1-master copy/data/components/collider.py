__author__ = 'justinarmstrong'

import pygame as pg
from .. import constants as c
from inspect import currentframe, getframeinfo

class Collider(pg.sprite.Sprite):
    """Invisible sprites placed overtop background parts
    that can be collided with (pipes, steps, ground, etc."""
    cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

    def __init__(self, x, y, width, height, name='collider'):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height)).convert()
        #self.image.fill(c.RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.state = None

