class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        if len(s3) != (len(s1) + len(s2)):
            return False
        dp = [[False for i in xrange(len(s2)+1)] for x in xrange(len(s1)+1)]
        dp[0][0] = True
        for i in xrange(1, len(s1)+1):
            dp[i][0] = dp[i-1][0] and s3[i-1] == s1[i-1]
        for i in xrange(1, len(s2)+1):
            dp[0][i] = dp[0][i-1] and s3[i-1] == s2[i-1]
        
        for i in xrange(1, len(s1)+1):
            for j in xrange(1, len(s2)+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
            
        return dp[len(s1)][len(s2)]
                

  

if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3t = "aadbbcbcac"
    s3f = "aadbbbaccc"
    so = Solution()
    print so.isInterleave(s1,s2,s3t)
    print so.isInterleave(s1,s2,s3f)