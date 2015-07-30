from collections import deque
import time
from threading import Thread
from threading import Lock
lock = Lock()

class HitCounter():
    def __init__(self):
        self.queue = deque()
    # lock on this ~/Dropbox/Programs/Python/Basics

    # More: we may not need to use queue, it depends on how often it hit
    # because popleft is O(1) * k(to skip), silcing is O(M) M items to keep

    def hit():
        timestamp = time.time()
        # timestamp % n machine
        while queue:
            if timestamp - queue[0] > 300:
                queue.popleft()
        queue.append(timestamp)
    
    def get_hit():
        return len(self.queue)


Queue = deque()

class HitThread(Thread):
    def __init__(self, sleep_time):
        super(HitThread, self).__init__()
        time.sleep(sleep_time)
        
    def run(self):
        lock.acquire()
        timestamp = time.time()
        # timestamp % n machine
        while Queue:
            if timestamp - Queue[0] > 3:
                Queue.popleft()
        Queue.append(timestamp)
        lock.release()

def hit_all():
    threads = []
    for i in range(3):
        t = HitThread(i)
        threads.append(t)
        t.start()
    print len(Queue)
    for t in threads:
        t.join()
    print len(Queue)
    
        
hit_all()
