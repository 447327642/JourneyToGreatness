// https://oj.leetcode.com/problems/reverse-integer/

// Reverse digits of an integer.
// Example1: x =  123, return  321
// Example2: x = -123, return -321
// click to show spoilers.
// Have you thought about this?
// Here are some good questions to ask before coding. Bonus points for you if you
// If the integer's last digit is 0, what should the output be? ie, cases such as
// Did you notice that the reversed integer might overflow? Assume the input is a
// 32-bit integer, then the reverse of 1000000003 overflows. How should you handle
// Throw an exception? Good, but what if throwing an exception is not an option?

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        long res = 0;
        while(x) {
            res = res*10 + x%10;
            x /= 10;
        }
	// carefull !!
        if (res > INT_MAX || res < INT_MIN)
            return 0;
	// it's ok to return long, but recommend int
        return (int)res;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
