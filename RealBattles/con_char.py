import unittest

def max_letter(string):
    if len(string) == 0:
        return ""
    res = ""
    res_cnt = 0
    curr = string[0]
    curr_cnt = 1
    for i in xrange(1, len(string)):
        if string[i] == curr:
            curr_cnt += 1
        else:
            if curr_cnt > res_cnt:
                res = curr
                res_cnt = curr_cnt
            curr = string[i]
            curr_cnt = 1
            
    if curr_cnt > res_cnt:
        res = curr
        res_cnt = curr_cnt

    return res

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(max_letter(""), "")
        
    def test2(self):
        self.assertEqual(max_letter("ab"), "a")
        
    def test3(self):
        self.assertEqual(max_letter("aab"), "a")
        
    def test4(self):
        self.assertEqual(max_letter("abb"), "b")
        
if __name__ == '__main__':
    unittest.main()
            
