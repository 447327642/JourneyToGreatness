#include <iostream>
#include <vector>

using namespace std;

/*
 Why Time Complexity is O(n)?
 The first round need traverse n elements,
 the second round need traverse n/2 elements,
 ...
 T(n) = n + n/2 + n/4 ... <= 2n = O(n)
 because q_select each time call one recursion.
 */
int partition(vector<int> &arr, int left, int right) {
    int p = left;
    int pivot = arr[p];
    for (int i = left+1; i < right; i++) {
	if (arr[i] < pivot) {
	    swap(arr[++p], arr[i]);
	}
    }
    swap(arr[p], arr[left]);    
    return p;
}

// find kth smallest element
int q_select(vector<int> arr, int k, int left, int right) {
    int idx = partition(arr, left, right);
    if (idx > k-1)
	return q_select(arr, k, left, idx);
    else if (idx < k-1)
	return q_select(arr, k-idx-1, idx, right);
    else
	return arr[idx];
}

int q_select(vector<int> arr, int k) {
    return q_select(arr, k, 0, arr.size());
}

int main(int argc, char *argv[])
{
    vector<int> arr = {9,6,1,4,2,5,3,7,8};
    cout<<q_select(arr, 3)<<endl;
    return 0;
}

