#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

#define DIR_X 0x001
#define DIR_Y 0x002
#define all(a) (a).begin(), (a).end()
/*
  Every point to remaining point manhattan distance sum is
  the score of this point.
  Caculate every point's score.
 */

struct point {
    int x, y;
    int total_score; // uninitialized, shortest
    point(int a, int b): x(a), y(b), total_score(0) {}
};

struct comp1 {
    bool operator()(const point &a, const point &b) {
        return a.x<b.x;
    }
};

struct comp2 {
    bool operator()(const point &a, const point &b) {
        return a.y<b.y;
    }
};

void set_fix_array(int n, int dir, vector<point> &points, vector<int> &prefix, vector<int> &suffix) {
    prefix.resize(n, 0);
    suffix.resize(n, 0);
    for (int i = 0; i < n; i++) {
        int val = dir == DIR_X ? points[i].x : points[i].y;
        prefix[i] = !i ? val : prefix[i-1] + val;
    }
    for (int i = n-1; i >= 0; i--) {
        int val = dir == DIR_X ? points[i].x : points[i].y;
        suffix[i] = i == n-1 ? val : suffix[i+1] + val;
    }
}

void add_score(int n, int dir, vector<point> &points, vector<int> &prefix, vector<int> &suffix) {
    for (int i = 0; i < n; i++) {
        point &p = points[i];
        int val = dir == DIR_X ? p.x : p.y;
        p.total_score += (!i ? 0 : (i*val - prefix[i-1])) + (i == n-1 ? 0 : (suffix[i+1] - ((n-i-1)*val)));
    }
}

// O(nlogn)
void calculate_all_manhattan_scores(vector<point> &points) {
    int n = points.size();
    vector<int> prefix, suffix;
    sort(all(points), comp1());
    set_fix_array(n, DIR_X, points, prefix, suffix);
    add_score(n, DIR_X, points, prefix, suffix);
    sort(all(points), comp2());
    set_fix_array(n, DIR_Y, points, prefix, suffix);
    add_score(n, DIR_Y, points, prefix, suffix);
}

void test(){
    vector<point> t1 = {point(1,2), point(1,4), point(3,5), point(4,2)};
    calculate_all_manhattan_scores(t1);
    for (auto p: t1)
        printf("point %d %d: score %d\n", p.x, p.y, p.total_score);
    // 10, 10, 12, 12
}


int main(void) {
    test();
}
