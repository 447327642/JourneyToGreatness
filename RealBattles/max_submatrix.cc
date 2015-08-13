#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <string>
#include <unordered_set>
#include <stack>
using namespace std;

class MaxSubMatrix {
private:
    int largestRectangleArea(vector<int> &height) {
	stack<int> s;
	int maxval = 0;
	int i = 0;
	while (i < height.size()) {
	    if (s.empty() || height[i] > height[s.top()]) {
		s.push(i);
		i++;
	    } else { // height[s.top] >= height[i]
		int t = s.top();
		s.pop();
		maxval = max(maxval, height[t] * (s.empty() ? i: i - s.top() - 1));
	    }
	}

	while (!s.empty()) {
	    int t = s.top();
	    s.pop();
	    maxval = max(maxval, height[t] * (s.empty() ? i: i - s.top() - 1));
	}
	return maxval;
    }
public:
    int max_mat(vector<vector<int> > &mat) {
	int m = mat.size();
	if (!m)
	    return 0;
        int n = mat[0].size();
	if (!n)
	    return 0;
	vector<vector<int> > height(m, vector<int>(n, 0));
	for (int i = 0; i < m; i++) {
	    for (int j = 0; j < n; j++) {
		if (mat[i][j] == 0) {
		    height[i][j] = 0;
		} else {
		    height[i][j] = (i == 0) ? 1 : height[i-1][j] + 1;
		}
	    }
	}
	int maxArea = 0;
	for (int i = 0; i < m; i++) {
	    maxArea = max(maxArea, largestRectangleArea(height[i]));
	}
	return maxArea;
    }
    
    void test() {
	vector<vector<int > > mat = {
	    {0,0,1,0},
	    {1,1,1,1},
	    {1,1,1,0},
	    {0,1,1,0}
	};
	cout<<max_mat(mat);
    }
};

int main(int argc, char *argv[])
{
    MaxSubMatrix msm;
    msm.test();
    return 0;
}
