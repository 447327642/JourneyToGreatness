class Solution:
    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        # if n % 3 == 0. In each turn, no matter how many coins the first 
        # player take(1<=k<=2), the second player take 3 - k coins.
        # So player 1 cannot win
        return n % 3 != 0
