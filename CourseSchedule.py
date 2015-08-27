# DFS: https://leetcode.com/discuss/37781/60ms-concise-python-solution-using-topological-sort
# delete the ndoe which indegree as 0: http://zhufangxing.com/2015/05/07/leetcode-ICourse%20Schedule/

import collections

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        # Build adjancy list
        if numCourses < 2:
            return True
        # from collections import defaultdict
        PATH = collections.defaultdict(list)
        for edge in prerequisites:
            PATH[edge[0]].append(edge[1])

        # A global set to mark valied node
        searched = set()
        for start in PATH.keys():
            if self.dfs(PATH, start, set(), searched):
                return False
        return True

    def dfs(self, PATH, curr, seen, searched):
        """ dfs each node
        Args:
            PATH, adjancy list
            curr, current node
            seen, a set to mark visited node of each edge[0]
            A global set to mark valied node
        Return:
            True if has cycle
        """
        if curr in searched:
            return False
        for x in PATH[curr]:
            if x in seen:
                return True
            seen.add(x)
            if self.dfs(PATH, x, seen, searched):
                return True
            # this branch has no cycle, back track to detect others
            seen.remove(x)
        # if reach here, it means the grach start since curr is secure
        searched.add(curr)
        return False


    def canFinish2(self, numCourses, prerequisites):
        """
        queue to store the node which indegree is 0
        """
        graph = collections.defaultdict(set)
        neighbors = collections.defaultdict(set)
        for course, pre in prerequisites:
            graph[course].add(pre)
            neighbors[pre].add(course)
        #stack = [n for n in range(numCourses) if not graph[n]]
        queue = collections.deque([n for n in range(numCourses) if not graph[n]])
        count = 0
        while queue:
            print queuex
            node = queue.popleft()
            count += 1
            for n in neighbors[node]:
                graph[n].remove(node)
                if not graph[n]:
                    queue.append(n)
        return count == numCourses

if __name__ == '__main__':
    so = Solution()
    print so.canFinish(6, [[1, 0], [3, 1], [4, 2], [2, 5]])
