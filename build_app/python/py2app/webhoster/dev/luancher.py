from multiprocessing import Queue, Process

def processor():
    setproctitle('%s - processor ' % ("webhoster2.py",))

    while True:
        time.sleep(1)
        do_stuff()

my_processor = Process(target=processor)
