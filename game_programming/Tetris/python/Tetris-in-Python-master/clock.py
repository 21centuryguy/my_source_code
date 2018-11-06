from time import clock
from inspect import currentframe, getframeinfo

class Clock:
    """set up a timer to record what is time to do"""
    from inspect import currentframe, getframeinfo
    cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

    def __init__(self, st):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        self.st = st
        self.last_drop = clock()
        self.last_move = clock()
        self.last_rotate = clock()
        self.last_left_down = clock()
        self.last_right_down = clock()
        self.last_quick_drop = clock()
        self.last_stop = clock()
        self.last_should_stop = None    # for detection of the stop at the very bottom
        self.stop_detection_started = False
        self.last_straight_drop = clock()

    def update_drop(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        self.last_drop = clock()

    def update_move(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        self.last_move = clock()

    def update_rotate(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
 
        self.last_rotate = clock()

    def update_left_down(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        self.last_left_down = clock()

    def update_right_down(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        self.last_right_down = clock()

    def update_quick_drop(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        self.last_quick_drop = clock()

    def update_stop(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        self.last_stop = clock()

    def update_should_stop(self, mode):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        if mode is True and self.stop_detection_started is False:
            self.last_should_stop = clock()
            self.stop_detection_started = True
        elif mode is None:
            self.stop_detection_started = False


    def update_straight_drop(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        self.last_straight_drop = clock()

    def is_time_to_drop(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        return ((clock() - self.last_drop) > self.st.time_drop)

    def is_time_to_quick_drop(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        return ((clock() - self.last_quick_drop) > self.st.time_quick_drop) and\
               ((clock() - self.last_stop) > self.st.time_before_drop)

    def is_time_to_move(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        return (clock() - self.last_move) > self.st.time_move

    def is_time_to_rotate(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        return (clock() - self.last_rotate) > self.st.time_rotate

    def is_time_to_quick_left(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        return (clock() - self.last_left_down) > self.st.time_to_quick

    def is_time_to_quick_right(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        return (clock() - self.last_right_down) > self.st.time_to_quick

    def is_time_to_straight_drop(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))

        return (clock() - self.last_straight_drop) > self.st.time_to_straight_drop

    def is_time_to_stop(self):
        cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))
        
        return  self.stop_detection_started and\
                ((clock() - self.last_should_stop) > self.st.time_stop)
