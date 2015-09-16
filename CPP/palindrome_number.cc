// https://oj.leetcode.com/problems/palindrome-number/

// Determine whether an integer is a palindrome. Do this without extra space.
// click to show spoilers.
// Some hints:
// Could negative integers be palindromes? (ie, -1)
// If you are thinking of converting the integer to string, note the restriction
// You could also try reversing an integer. However, if you have solved the
// problem "Reverse Integer", you know that the reversed integer might overflow.
// There is a more generic way of solving this problem.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0) {
	    return false;
	}
	int len = 1;
	for (len = 1; (x/len) >= 10; len*= 10);
	
	while (x!=0) {
	    int left = x / len;
	    int right = x % 10;
	    if (left != right) {
		return false;
	    }
	    x = (x%len) / 10;
	    len /= 100;
	}
	return true;
    }

    bool isPalindrome(int x) {
	// problem: might overflow
	return (x >= 0 && x == reverse(x));
    }
private:
    int reverse(int x) {
	int y = 0;
	int n;
	while (x) {
	    n = x%10;
	    y = y*10 + n;
	    x /= 10;
	}
	return y;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
