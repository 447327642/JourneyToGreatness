#include <iostream>
#include <queue>
#include <vector>

struct entry {
  std::string username;
  int login;
  int logout;
};
class OnlinePeople {
 private:
  struct cmp {
    bool operator()(const std::pair<int, int> &x,
                    const std::pair<int, int> &y) {
      return x.first > y.first;
    }
  };

 public:
    std::vector<std::pair<int, int> > count_users(std::vector<entry> log) {
    std::priority_queue<std::pair<int, int>,
                        std::vector<std::pair<int, int> >, cmp> pq;
    int cnt = 0;
    std::vector<std::pair<int, int> > result;
    for (auto en : log) {
      pq.push(std::make_pair(en.login, 1));
      pq.push(std::make_pair(en.logout, -1));
    }
    while (!pq.empty()) {
      auto event = pq.top();
      pq.pop();
      cnt += event.second;
      if (result.size() > 0 && event.first == result.back().first) {
        result.back().second = cnt;
      } else {
        result.push_back(std::make_pair(event.first, cnt));
      }
    }
    return result;
  }
};

int main(int argc, char *argv[]) {
  entry e1 = {"Alice", 3, 11};
  entry e2 = {"Bob", 6, 8};
  entry e3 = {"Carol", 11, 12};
  std::vector<entry> log({e1, e2, e3});
  OnlinePeople op;
  std::vector<std::pair<int, int> > result = op.count_users(log);
  for (auto line : result) {
    std::cout << line.first << " " << line.second << std::endl;
  }
  return 0;
}

