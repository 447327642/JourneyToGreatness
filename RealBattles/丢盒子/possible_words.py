from collections import defaultdict

# Time complexity

def possible_words(numbers, dic):
    """
    Args:
        numbers: a string of 7 digits
        dic: a set of words
    Returns:
        res: a list of possible words
    """
    tab = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    res = []
    dfs(tab, numbers, res, "", [], dic)
    return res

# one query, dfs
def dfs(tab, numbers, res, buff, res_buff, dic):
    """ depth first search for possible words
    Args:
        tab: a dictionary of number -> chars map
        numbers: remaining numbers to handle
        res: result (list of string)
        buff: current possible word prefix
        dic: given set of dictionary
    """
    if len(numbers) == 0:
        if buff in dic:
            if len(buff) == 7:
                res.append(buff)
            else:
                res_buff.append(buff)
                res.append(' '.join(res_buff))
                res_buff.pop()
        return


    if len(buff) >= 3:
        if buff in dic:
            #res.append(buff)
            res_buff.append(buff)
            for c in tab[numbers[0]]:
                dfs(tab, numbers[1:], res, c, res_buff, dic)
            res_buff.pop()


    for c in tab[numbers[0]]:
        dfs(tab, numbers[1:], res, buff + c, res_buff, dic)


#  more than one query, preprocessing dictionary
def reverse_index(numbers, dic):
    new_dict = defaultdict(list)
    for word in dic:
        new_dict[str2num(word)].append(word)
    res = []
    dfs2(0, numbers, new_dict, [], res)
    return res

def dfs2(i, numbers, new_dict, buff, res):
    if numbers == '':
        res.append(' '.join(buff))
        return

    for i in range(3, len(numbers)+1):
        if numbers[:i] in new_dict:
            for word in new_dict[numbers[:i]]:
                buff.append(word)
                dfs2(i, numbers[i:], new_dict, buff, res)
                buff.pop()
    return



def str2num(string):
    num = []
    for c in string:
        num.append(char2digit(c))
    return ''.join(num)

def char2digit(ch):
    ch = ch.lower()
    if 'a' <= ch <= 'c':
        return '2'
    elif 'd' <= ch <= 'f':
        return '3'
    elif 'g' <= ch <= 'i':
        return '4'
    elif 'j' <= ch <= 'l':
        return '5'
    elif 'm' <= ch <= 'o':
        return '6'
    elif 'p' <= ch <= 's':
        return '7'
    elif 't' <= ch <= 'v':
        return '8'
    elif 'w' <= ch <= 'z':
        return '9'



def test():
    dic = set(["nice", "car", "ohafabs", "ohcf", "bbs", "wilsonab"])
    num = "6423227"
    print possible_words(num, dic)
    print reverse_index(num, dic)

test()
