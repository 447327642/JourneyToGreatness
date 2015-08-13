#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <unordered_set>
using namespace std;

struct node {
    vector<node *> children;
};
class Detect_cycle {
private:
    bool dfs(node *n, 	unordered_set<node *> &vis, unordered_set<node *> &rou) {
	vis.insert(n);
	rou.insert(n);
	for (node *c: n->children) {
	    if (!vis.count(c) && dfs(c, vis, rou)) {
		return true;
	    }
	    else if (rou.count(c)) {
		return true;
	    }		
	}
	rou.erase(n);
	return false;
    }
public:
    bool has_cycle_directed(node *n) {
	unordered_set<node *> visit, route;
	return dfs(n, visit, route);
    }
    void test() {
        vector<node> nodes(4, node());
        nodes[0].children.push_back(&nodes[1]);
        nodes[0].children.push_back(&nodes[2]);
        nodes[1].children.push_back(&nodes[3]);
        nodes[2].children.push_back(&nodes[3]);

	printf("%d\n", has_cycle_directed(&nodes[0]));
    }
};

int main(int argc, char *argv[])
{
    Detect_cycle dc;
    dc.test();
    return 0;
}
