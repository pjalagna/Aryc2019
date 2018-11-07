#!/usr/bin/python

# main thread process
import Queue
import threading
import time
exitFlag = 0
        

threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = Queue.Queue(10)

threads = []

# Create new threads
threadID = 1
for tName in threadList:
    thread = myThread(threadID, tName, workQueue) # class(init paras)
    thread.start() # calls class.run()
    threads.append(thread) # array of names for exit process
    threadID += 1

# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
    print('q',word)
queueLock.release()

# Wait for queue to empty
while not workQueue.empty():
    pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
    t.join()
print "Exiting Main Thread \n"

#--- routine on main thread
def process_data(threadName, q):
    while not exitFlag: # variable in main thread visiable in each thread
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s \n" % (threadName, data)
        else:
            queueLock.release()
        #endif
        time.sleep(1)
    #wend
#end process_data
#-----------------------------------------------------
#-------------sub process class -------------------------------

class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        """ facade to call process_data """
        print "Starting " + self.name + '\n'
        process_data(self.name, self.q) # process in main thread
        print "Exiting " + self.name + '\n'
    #end run
#end myThread class
#--------------------------------------------------------
