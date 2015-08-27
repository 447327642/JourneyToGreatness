"""
1. sort by start time
2. if can put in current, put in the back, else, create another room
"""


K = [[1, 4], [3, 5], [4, 6], [6, 7], [1, 9], [10, 11], [6, 10]]
K = sorted(K, key=lambda a: a[0])
result1 = []
for interval in K:
    new_room = True
    for arranged in result1:
        # arranged may like [[1,4], [4, 6]], now we have [6, 7] as interval
        if interval[0] >= arranged[-1][-1]:
            arranged.append(interval)
            new_room = False
            break
    if new_room:
        result1.append([interval])

for l in result1:
    print l

# rewrite

class Time:
    def __init__(self, start, end):
        assert(start <= end)
        self.start = start
        self.end = end

L = []
for i in K:
    L.append(Time(i[0], i[1]))
L = sorted(L, key = lambda a: a.start)
result = []
for interval in L:
    new_room = True
    for arranged in result:
        if interval.start >= arranged[-1].end:
            arranged.append(interval)
            new_room = False
            break
    if new_room:
        result.append([interval])
for l in result:
    for v in l:
        print "(%d, %d) " % (v.start, v.end),
    print
