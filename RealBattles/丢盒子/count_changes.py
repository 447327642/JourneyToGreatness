def count(S, m, n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if m <= 0 and n >= 1:
        return 0
    return count(S, m - 1, n) + count(S, m, n - S[m-1])

def test():
    S = [1, 5, 10, 25]
    #print (count(S, len(S), 4))
    print count2(S, 30)

def count2(coins, n):
    dp = [0 for x in xrange(n+1)]
    dp[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], n+1):
            dp[j] += dp[j - coins[i]]
            print dp
    return dp[n]

test()
