class Solution:
    # @return a list of strings, [s1, s2]

    def letterCombinations(self, digits):
        tab = {'2':'abc', '3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        words_dict = {}
        res = []
        self.dfs(tab, digits, res, "")
        return res

    def dfs(self, tab, digits, res, buff, words_dict):
        """
        Args:
            tab: convert table
            digits: input string
            res: result list
            buff: buffer to store intermediate string
            cnt: buff length count
        Returns:
            None
        """
        if len(digits) == 0:
            if buff in words_dict:
                res.append(buff)
            return

        for c in tab[digits[0]]:
            if buff+c in words_dic:
                self.dfs(tab, digits[1:], res, "")
            self.dfs(tab, digits[1:], res, buff+c)
            # may duplicate
            # use word break method
            

END = '$'

def make_trie(words):
    root = {}
    for word in words:
        t = root
        for c in word:
            if c not in t:
                t[c] = {}
            t = t[c]
        t[END] = {}
    return root

import unittest
# another
K = [[1, 4], [3, 5], [4, 6], [6, 7], [1, 9], [10, 11], [6, 10]]
K = sorted(K, key=lambda a: a[0])
result = []
for interval in K:
    new_room = True
    for arranged in result:
        # arranged may like [[1,4], [4, 6]], now we have [6, 7] as interval
        if interval[0] >= arranged[-1][-1]:
            arranged.append(interval)
            new_room = False
            break
    if new_room:
        result.append([interval])

for l in result:
    print l


def wordBreak(self, s, dic):
    dp = [False] * (len(s)+1)
    dp[0] = True
    for i in range(len(s)):
        if dp[i] is False:
            continue
        for j in dic:
            if j == s[i:i+len(j)]:
                dp[i+len(j)] = True
            continue
    return dp[len(s)]

class testSchedult(unittest.TestCase):
    def test_simple(self):
        #K = [[1, 4], [3, 5], [4, 6], [6, 7], [1, 9], [10, 11], [6, 10]]
        self.assertEqual(1,1)

if __name__ == '__main__':
    unittest.main()
        

        
            



# if __name__ == '__main__':
#     so = Solution()
#     print so.letterCombinations("23")
