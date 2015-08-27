#include <iostream>
#include <vector>

using namespace std;
vector<int> coins = {3, 2, 1};

void print_v(vector<int> v) {
    for (auto i : v)
        cout<<i<<" ";
    cout<<endl;
}

// worst
void make_change2(int money, vector<int> &buff, int start, const vector<int> &coins) {
    if (money == 0) {
        print_v(buff);
        return;
    }
    else if (money < 0) {
        return;
    }
    for (size_t i = start; i < coins.size(); i++) {
        if (money >= coins[i]) {
            buff.push_back(coins[i]);
            make_change2(money-coins[i], buff, i, coins);
            buff.pop_back();
        }
    }
}

int main(void) {
    
    vector<int> buff;
    make_change2(4, buff, 0, coins);
}
