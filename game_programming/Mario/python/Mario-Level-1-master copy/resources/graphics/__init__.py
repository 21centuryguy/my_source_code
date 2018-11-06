__author__ = 'justinarmstrong'
from inspect import currentframe, getframeinfo
cf = currentframe(); print("\n[ DEBUG ] [ function ] " + str(cf.f_code))