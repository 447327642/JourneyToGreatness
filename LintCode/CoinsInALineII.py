class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        if len(values) <= 2:
            return True
        sum1 = 0
        sum2 = 0
        turn = True
        # greedy
        i = 0
        while i < len(values):
            curr = values[i]
            if i + 1 < len(values) and values[i+1] >= values[i]:
                curr += values[i+1]
                i += 1
            if turn:
                sum1 += curr
            else:
                sum2 += curr
            i += 1
            turn = not turn
        return sum1 > sum2


if __name__ == '__main__':
    so = Solution()
    so.firstWillWin([1, 2, 4])
