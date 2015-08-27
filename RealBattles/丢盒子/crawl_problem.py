import requests
from collections import deque



class Crawler:
    def __init__(self, init_url):
        self.queue = deque([init_url])
        self.cnt = 0
        self.link_set = set()
        
    def get_links(self, page):
        """ parse current page, retrive all href links in current page
            # some link need to normalize (relative path)
            # IO Exceptions
        """
        try:
            # parse and get page
        except:
            # handle
        pass

    def crawler(self):
        while self.queue:
            curr = self.queue.pop()
            print (curr)
            self.cnt += 1
            
            links = get_links(link)
            for l in links:
                if l not in self.link_set:
                    self.link_set.add(l)
                    self.queue.append(l)
            
            
    
""" Then make it multiple threaded.
    
    1. Queue (put, get, not q.empty()) Thread safe
    2. link_set lock, to check in it or add it

# task_done: indicate that a formerly enqueued task is completed
# Key: crawl function
"""
