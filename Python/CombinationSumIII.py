class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        res = []
        def dfs(k, n, start, curr):
            if start > n:
                return
            print k, n, start, curr
            if k == 1:
                if n not in curr and n <= 9:
                    curr.add(n)
                    res.append(list(curr))
                    curr.remove(n)
                return
            for i in range(start, 9 + 1):
                curr.add(i)
                dfs(k - 1, n - i, i + 1, curr)
                curr.remove(i)
        dfs(k, n, 1, set())
        return res


if __name__ == '__main__':
    so = Solution()
    print so.combinationSum3(2, 6)
