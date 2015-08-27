# -*- coding: utf-8 -*-

ByOne = [
"zero",
"one",
"two",
"three",
"four",
"five",
"six",
"seven",
"eight",
"nine",
"ten",
"eleven",
"twelve",
"thirteen",
"fourteen",
"fifteen",
"sixteen",
"seventeen",
"eighteen",
"nineteen"
]

ByTen = [
"zero",
"ten",
"twenty",
"thirty",
"forty",
"fifty",
"sixty",
"seventy",
"eighty",
"ninety"
]

def int2text(n):
    assert(isinstance(n, (int, long)))
    assert(0 <= n <= 999)
    if n <= 19:
        return ByOne[n]
    elif n <= 99:
        q, r = divmod(n, 10) # q, r  = n/10, n%10
        return ByTen[q] + (" " + int2text(r) if r else "")
    else:
        q, r = divmod(n, 100)
        return ByOne[q] + " hundred" + (" and " + int2text(r) if r else "")
    # add () 是因为如果是整十，整百，不要 and 或者后面的一套东西
for i in range(901):
    print int2text(i)
