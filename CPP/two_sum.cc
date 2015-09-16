// https://oj.leetcode.com/problems/two-sum/

// Given an array of integers, find two numbers such that they add up to a
// The function twoSum should return indices of the two numbers such that they add
// up to the target, where index1 must be less than index2. Please note that your
// You may assume that each input would have exactly one solution.
// Input: numbers={2, 7, 11, 15}, target=9
// Output: index1=1, index2=2

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            int t = target - nums[i];
            if (map.find(t) != map.end()) {
                return vector<int>{map[t]+1, i+1};
            } else {
                map[nums[i]] = i;
            }
        }
        return vector<int>{-1, -1};
    }
};


int main(int argc, char *argv[])
{

    return 0;
}
