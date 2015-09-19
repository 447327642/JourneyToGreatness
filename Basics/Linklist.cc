#include <iostream>
#include <algorithm>

using namespace std;

struct ListNode{
    int val;
    ListNode *next;
    ListNode(int x): val(x), next(nullptr) {}
};


ListNode* reverse(ListNode *head) {
    if (!head)
	return nullptr;
    ListNode *prev = head, *succ = head, *now, *tail = head;
    while (succ) {
	now = succ;
	succ = succ->next;
	now->next = prev;
	prev = now;
    }
    // tail->next is itself, let's point it to nullptr
    tail->next = nullptr;
    return now; // or prev
}


bool detectCycle(ListNode *head) {
    if (!head)
	return false;
    ListNode *fast = head, *slow = head;
    while (fast and fast->next) {
	fast = fast->next->next;
	slow = slow->next;
	if (fast == slow)
	    return true;
    }
    return false;
}

int main(int argc, char *argv[])
{
    ListNode *head = new ListNode(1);
    head->next = new ListNode(2);
    head->next->next = new ListNode(3);
    ListNode *p = reverse(head);
    while (p){
	cout<<p->val<<endl;
	p = p->next;
    }
    return 0;
}

