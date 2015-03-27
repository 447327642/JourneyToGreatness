// https://oj.leetcode.com/problems/climbing-stairs/

// You are climbing a stair case. It takes n steps to reach to the top.
// Each time you can either climb 1 or 2 steps. In how many distinct ways can you

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2)
            return n;
        int dp[n+1];
        dp[1] = 1, dp[2] = 2;
        for (int i = 3; i <= n; i++)
            dp[i] = dp[i-2] + dp[i-1];
        return dp[n];
    }
}

int main(int argc, char *argv[])
{

    return 0;
}
