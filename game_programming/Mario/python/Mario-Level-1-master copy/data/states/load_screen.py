__author__ = 'justinarmstrong'

from .. import setup, tools
from .. import constants as c
from .. import game_sound
from ..components import info
from inspect import currentframe, getframeinfo

class LoadScreen(tools._State):
    def __init__(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        tools._State.__init__(self)

    def startup(self, current_time, persist):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        self.start_time = current_time
        self.persist = persist
        self.game_info = self.persist
        self.next = self.set_next_state()

        info_state = self.set_overhead_info_state()

        self.overhead_info = info.OverheadInfo(self.game_info, info_state)
        self.sound_manager = game_sound.Sound(self.overhead_info)


    def set_next_state(self):
        """Sets the next state"""
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        return c.LEVEL1

    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        return c.LOAD_SCREEN


    def update(self, surface, keys, current_time):
        """Updates the loading screen"""
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        if (current_time - self.start_time) < 2400:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)

        elif (current_time - self.start_time) < 2600:
            surface.fill(c.BLACK)

        elif (current_time - self.start_time) < 2635:
            surface.fill((106, 150, 252))

        else:
            self.done = True




class GameOver(LoadScreen):
    """A loading screen with Game Over"""


    def __init__(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        super(GameOver, self).__init__()


    def set_next_state(self):
        """Sets next state"""
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        return c.MAIN_MENU

    def set_overhead_info_state(self):
        """sets the state to send to the overhead info object"""
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        return c.GAME_OVER

    def update(self, surface, keys, current_time):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        self.current_time = current_time
        self.sound_manager.update(self.persist, None)

        if (self.current_time - self.start_time) < 7000:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        elif (self.current_time - self.start_time) < 7200:
            surface.fill(c.BLACK)
        elif (self.current_time - self.start_time) < 7235:
            surface.fill((106, 150, 252))
        else:
            self.done = True


class TimeOut(LoadScreen):
    """Loading Screen with Time Out"""


    def __init__(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        super(TimeOut, self).__init__()

    def set_next_state(self):
        """Sets next state"""
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        if self.persist[c.LIVES] == 0:
            return c.GAME_OVER
        else:
            return c.LOAD_SCREEN

    def set_overhead_info_state(self):
        """Sets the state to send to the overhead info object"""
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        return c.TIME_OUT

    def update(self, surface, keys, current_time):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        self.current_time = current_time

        if (self.current_time - self.start_time) < 2400:
            surface.fill(c.BLACK)
            self.overhead_info.update(self.game_info)
            self.overhead_info.draw(surface)
        else:
            self.done = True









