# -*- coding: utf-8 -*-

lt = [1,4,-3,2,6,1]

# 前缀和法
def get_sum(lt, target):
    """ Return a start and end index
    """
    lookup = {0:-1} # important 如果一个数自己就是 target。
    prefix_sum = 0
    res = []
    for i in range(len(lt)):
        key = target - lt[i]
        if key in lookup:
            if lookup[key] == -1:
                res.append([i, i])
            else:
                res.append([lookup[key], i])
        else:
            curr_sum = prefix_sum + lt[i]
            lookup[curr_sum] = i
    return res
    
print get_sum(lt, 1)
# 尺缩法  用于 non-negtive
