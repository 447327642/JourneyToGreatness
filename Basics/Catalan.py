#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
http://ilovers.sinaapp.com/article/catalan%E6%95%B0
C0 = 1 ;
Cn = sum(Ci · C(n-1-i);

Cn = C(2n, n)/(n+1)
其中C(m,n)是 n 个不同的数中取 m 个数形成的组合数

http://stackoverflow.com/questions/4941753/is-there-a-math-ncr-function-in-python
'''

import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def Catalan(n):
    return nCr(2 * n, n) / (n + 1)


if __name__ == '__main__':
    print nCr(10,5)
    print Catalan(5)
