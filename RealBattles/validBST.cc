#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <unordered_set>
using namespace std;

struct tree_node {
    int val;
    tree_node *l, *r;
    tree_node(int val): val(val), l(nullptr), r(nullptr) {}
};

class Valid_BST {

private:
    bool is_valid(tree_node *root, int low, int up) {
	if (root == nullptr)
	    return true;
	if (root->val <= low || root->val >= up)
	    return false;
	return is_valid(root->l, low, root->val) && is_valid(root->r, root->val, up);
    }

public:    
    bool is_valid_BST(tree_node *root) {
	return is_valid(root, INT_MIN, INT_MAX);
    }
    void test() {
	tree_node root(6), n2(2), n1(1), n3(3), n8(8), n7(7);
	root.l = &n2;
	root.r = &n8;
	n8.l = &n7;
	n2.l = &n1;
	n2.r = &n3;
	printf("%d\n", is_valid_BST(&root));
	    
    }
};
 
int main(int argc, char *argv[])
{
    Valid_BST valid;
    valid.test();
    return 0;
}
