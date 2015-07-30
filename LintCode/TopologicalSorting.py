# TLE in case 15
# class DirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    """
    @param graph: A list of Directed graph node
    @return: A list of integer
    """
    def topSort(self, graph):
        # write your code here
        stack = []
        visited = set()
        for node in graph:
            node.neighbors = set(node.neighbors)
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for n in graph:
                    if node in n.neighbors:
                        dfs(n)
                stack.append(node)
            return
                
        for node in graph:
            dfs(node)
        return stack
