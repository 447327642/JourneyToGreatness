#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
    
private:
    vector<string> find_next(string curr, unordered_set<string> &dict) {
        vector<string> res;
        for (int i = 0; i < curr.size(); i++) {
            char tmp = curr[i];
            for (char c = 'a'; c <= 'z'; c++) {
                if (c == tmp)
                    continue;
                curr[i] = c;
                if (dict.count(curr)) {
                    res.push_back(curr);
                    dict.erase(curr);
                }
            }
            curr[i] = tmp;
        }
        return res;
    }
public:
    int ladderLength(string beginWord, string endWord, unordered_set<string>& wordList) {
        queue<pair<string, int>> q;
        q.push(make_pair(beginWord, 1));
        while (!q.empty()) {
            string curr = q.front().first;
            int count = q.front().second;
            if (curr == endWord)
                return count;
            q.pop();
            vector<string> next_words = find_next(curr, wordList);
            for (auto word: next_words) {
                q.push(make_pair(word, count+1));
            }
        }
        return 0;
    }
};

int main(int argc, char *argv[])
{

    return 0;
}
