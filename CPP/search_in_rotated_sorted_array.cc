// https://oj.leetcode.com/problems/search-in-rotated-sorted-array/

// Suppose a sorted array is rotated at some pivot unknown to you beforehand.
// (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
// You are given a target value to search. If found in the array return its index,
// You may assume no duplicate exists in the array.

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    int search(vector<int> &A, int target) {
        int left = 0, right = A.size() - 1;
	while (left <= right) {
	    int mid = left + (right - left) / 2;
	    if (A[mid] == target)
		return mid;
	    else if (A[left] <= A[mid]) {
		if (A[left] <= target && target < A[mid])
		    right = mid - 1;
		else
		    left = mid + 1;      
	    }
	    else {
		if (A[mid] < target && target <= A[right]) 
		    left = mid + 1;		    
                else
		    right = mid - 1;
	    }
	}
	return -1;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
