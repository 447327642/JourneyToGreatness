# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph
    def connectedSet(self, nodes):
        # Write your code here
        if len(nodes) == 0:
            return []
        visited = set()
        res = []

        from collections import deque
        def bfs(node):
            if node in visited:
                return
            queue = deque()
            queue.append(node)
            visited.add(node)
            buff = []
            while queue:
                cur = queue.popleft()
                buff.append(cur.label)
                for nb in cur.neighbors:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
            res.append(buff)
        for node in nodes:
            bfs(node)    
            
        return [sorted(c) for c in res]
                    
    
def test():
    na = UndirectedGraphNode('A')
    nb = UndirectedGraphNode('B')
    nc = UndirectedGraphNode('C')
    nd = UndirectedGraphNode('D')
    ne = UndirectedGraphNode('E')

    na.neighbors.extend([nb, nd])
    nb.neighbors.extend([na, nd])
    nd.neighbors.extend([na, nb])

    nc.neighbors.extend([ne])
    ne.neighbors.extend([nc])

    so = Solution()
    print so.connectedSet([na, nb, nc, nd, ne])
    
    
if __name__ == '__main__':
    test()
