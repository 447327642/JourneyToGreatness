alphabet = 'abcdefghijklmnopqrstuvwxyz'

def solution(S, T):
    if S == T:
        return "NOTHING"
    splits = [(S[:i], S[i:]) for i in range(len(S) + 1)]
    for a, b in splits:
        if b and a + b[1:] == T:
            return "DELETE " + b[0]
    for c in alphabet:
        for a, b in splits:
            if a + c + b == T:
                return "INSERT " + c
    for a, b in splits:
        if len(b) > 1:
            if a + b[1] + b[0] + b[2:] == T:
                return "SWAP %s %s" % (b[0], b[1])
    return "IMPOSSIBLE"


def solution2(A, K):
    n = len(A)
    best = 0
    count = 0
    for i in xrange(n - K - 1):
        if (A[i] == A[i + 1]):
            count = count + 1
        else:
           count = 0
        best = max(best, count)
    result = min(n, best + 1 + K)
    
    return result


def test_solution2():
    A = [1, 1, 1, 1, 1, 1]
    K = 2
    print solution2(A, K)
    print solution2([1,1,3,3,3,4,5,5,5,5], 2) == 5
    print solution2([1, 1, 1, 1, 1, 1], 6) 
    print solution2([1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4], 4) == 8

    



if __name__ == '__main__':
    S = "nice"
    T = "niece"
    # print solution(S, T)
    # print solution("form", "from")
    # print solution("o", "odd")
    test_solution2()
