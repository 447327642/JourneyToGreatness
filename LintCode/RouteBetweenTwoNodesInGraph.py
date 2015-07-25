tion for a Directed graph node
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @param s: the starting Directed graph node
    @param t: the terminal Directed graph node
    @return: a boolean value
    """
    def hasRoute(self, graph, s, t):
        # write your code here
        if len(s.neighbors) == 0:
            return False
        if s.label == t.label:
            return True
        visited = set()
        from collections import deque
        queue = deque([s])
        visited.add(s.label)
        while queue:
            curr = queue.popleft()
            if curr.label == t.label:
                return True
            for node in curr.neighbors:
                if node.label not in visited:
                    visited.add(node.label)
                    queue.append(node)
        return False

    def hasRoute2(self, graph, s, t):
        # write your code here
        if len(s.neighbors) == 0:
            return False
        if s.label == t.label:
            return True
        visited = set()
        def dfs(curr):
            if curr.label == t.label:
                return True
            visited.add(curr)
            for node in curr.neighbors:
                if node not in visited:
                    if dfs(node):
                        return True
        if dfs(s):
            return True
        return False
