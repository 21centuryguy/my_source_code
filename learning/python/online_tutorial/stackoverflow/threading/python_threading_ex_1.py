"""
https://stackoverflow.com/questions/2957116/make-2-functions-run-at-the-same-time
https://tecadmin.net/get-current-date-time-python/
"""

from threading import Thread
import datetime

def func1():
    currentDT = datetime.datetime.now()
    print ('Working from func1 : ', str(currentDT))

def func2():
    currentDT = datetime.datetime.now()
    print ('Working from func2 : ', str(currentDT))

def func3():
    currentDT = datetime.datetime.now()
    print ('Working from func3 : ', str(currentDT))

def func4():
    currentDT = datetime.datetime.now()
    print ('Working from func4 : ', str(currentDT))

def func5():
    currentDT = datetime.datetime.now()
    print ('Working from func5 : ', str(currentDT))

def func6():
    currentDT = datetime.datetime.now()
    print ('Working from func6 : ', str(currentDT))

def func7():
    currentDT = datetime.datetime.now()
    print ('Working from func7 : ', str(currentDT))

def func8():
    currentDT = datetime.datetime.now()
    print ('Working from func8 : ', str(currentDT))

def func9():
    currentDT = datetime.datetime.now()
    print ('Working from func9 : ', str(currentDT))

def func10():
    currentDT = datetime.datetime.now()
    print ('Working from func10 : ', str(currentDT))

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()
    Thread(target = func3).start()
    Thread(target = func4).start()
    Thread(target = func5).start()
    Thread(target = func6).start()
    Thread(target = func7).start()
    Thread(target = func8).start()
    Thread(target = func9).start()
    Thread(target = func10).start()
