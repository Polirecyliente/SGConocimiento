#!/usr/bin/python3
#   Multithreading

#T# import the threading module
import threading
import time

#T# create a lock to synchronize threads with Lock()
syncLock = threading.Lock()

#T# inherit from the Thread class to make thread objects
class hereThread(threading.Thread):

#T# call the original Thread constructor but also override __init__
    def __init__(self,threadID,name,counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

#T# override run() to define what each thread does
    def run(self):

#T# each thread acquires the lock with acquire()
        syncLock.acquire()
        print("Starting " + self.name)
        threadFun1(self.name,self.counter,0.2)
        print("Exiting " + self.name)

#T# at the end of the thread release the lock with release()
        syncLock.release()

#T# this function will be executed by the threads
def threadFun1(threadName,iters,delay):
    cou1 = 0
    while cou1 < iters:
        time.sleep(delay)
        cou1 += 1
        print("%s -> %s" % (threadName,time.ctime(time.time())))

#T# instantiate the thread objects
FThread = hereThread(1,"FirstThread",2)
SThread = hereThread(2,"SecondThread",5)
TThread = hereThread(3,"ThirdThread",4)

#T# start the threads with start()
FThread.start()
SThread.start()
TThread.start()

#T# the main thread waits for a thread to end with join()
FThread.join()

#T# several method from the threading module
print("Amount of threads:",threading.active_count())
print("Threads:",threading.enumerate())
print("The current thread is:",threading.current_thread())
print("is the SecondThread alive?",SThread.isAlive())
SThread.setName("HomieYoshThread")
print("The name of the SecondThread is:",SThread.getName())

print("Exiting MainThread")