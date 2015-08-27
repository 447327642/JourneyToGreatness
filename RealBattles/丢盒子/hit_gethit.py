from collections import deque
import time
from threading import Thread
from threading import Lock
# lock = Lock()

# How to scale it
# 拓展问了如果是multithreading怎么办，答用mutex lock gethit 和 loghit，又被问说如果loghit可以share，但gethit不能怎么办，答可以让每个thread maintain自己的数组，然后gethit 把这些sum up起来。

class HitCounter():
    def __init__(self):
        self.queue = deque()
    # lock on this ~/Dropbox/Programs/Python/Basics

    # More: we may not need to use queue, it depends on how often it hit
    # because popleft is O(1) * k(to skip), silcing is O(M) M items to keep
    # if QPS is frequent, use binary search to get the upper bound

    def hit(self):
        timestamp = time.time()
        # timestamp % n machine
        self.queue.append(timestamp)
        while self.queue and timestamp - self.queue[0] > 10:
            self.queue.popleft()

            
    def get_hit(self):
        timestamp = time.time()
        while self.queue and timestamp - self.queue[0] > 10:
            self.queue.popleft()
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
    
        


def test():
    hc = HitCounter()
    hc.hit()
    hc.hit()
    time.sleep(3)
    hc.hit()
    time.sleep(2)
    hc.hit()
    print hc.get_hit(), 4
    hc.hit()
    hc.hit()
    time.sleep(6)
    print hc.get_hit(), 4
    
test()
