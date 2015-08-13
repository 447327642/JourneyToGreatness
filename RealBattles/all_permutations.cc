#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <string>
#include <unordered_set>
using namespace std;

class Permutation {
private:
    void dfs(const string s, string buff, vector<string> &res) {
	//cout<<"show: "<<s<<" "<<buff<<" "<<endl;
	if (buff.size() == s.size()) {
	    res.push_back(buff);
	    return;
	}
	for (auto i: s) {
	    //auto p = find(s.begin(), s.end(), i);
	    if (buff.find(i) == string::npos) {
		buff.push_back(i);
		dfs(s, buff, res);
		buff.pop_back();
	    }
	}
    }
public:
    vector<string> permute(string s) {
	string buff;
	vector<string> res;
	dfs(s, buff, res);
	return res;
    }
    void test() {
        string s = "bca";
	auto res = permute(s);
	for (auto l: res)
	    cout<<l<<endl;
    }
};

int main(int argc, char *argv[])
{
    Permutation p;
    p.test();
    return 0;
}

