#include <iostream>
#include <algorithm>

using namespace std;

void move01() {
    //int arr[] = {1,0,0,1,0,1,0,0,1,0};
    int arr[] = {1,1,1,1,1,0};
    int left = 0, right = sizeof(arr)/sizeof(int) - 1;
    while (left < right) {
	while (arr[left] == 0)
	    left++;
	while (arr[right] == 1)
	    right--;
	if (left < right)
	    swap(arr[left], arr[right]);
    }
    for (int i = 0; i < sizeof(arr)/sizeof(int); i++) {
	cout<<arr[i];
    }
    cout<<endl;
}



int main(int argc, char *argv[]) {
    move01();

    return 0;
}
