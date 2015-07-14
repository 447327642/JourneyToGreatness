from collections import defaultdict

def match(pat, text):
    """ determine whether text match pat
    Args:
        pat, text: string
    Returns:
        Bool: match or not
    """
    if len(pat) > len(text):
        return False
    pat2text = defaultdict(str)
    text2pat = defaultdict(str)
    return matchHelper(pat, 0, text, 0, pat2text, text2pat)
    
def matchHelper(pat, patIdx, text, textIdx, pat2text, text2pat):
    """ recursively match string
    Args:
       pat, text: given pattern and text string
       patIdx, textIdx: index of current position, before index is matched parts
       pat2text, text2pat: dict of pat to text, text to pattern, because two pattern
                           cannot map to same string
    Returns:
       Bool: match or not
    """
    if patIdx == len(pat) and textIdx == len(text):
        return True
    if patIdx == len(pat) or textIdx == len(text):
        return False

    cur_pat = pat[patIdx]
    if cur_pat in pat2text:
        to_match = pat2text[cur_pat]
        if textIdx + len(to_match) > len(text) or \
           to_match != text[textIdx: textIdx+len(to_match)]:
            return False
        else:
            textIdx += len(to_match)
        if to_match not in text2pat or cur_pat != text2pat[to_match]:
            return False
        return matchHelper(pat, patIdx+1, text, textIdx, pat2text, text2pat)
    else:
        found = False
        for i in range(textIdx, len(text)):
            to_match = text[textIdx: i+1]
            pat2text[cur_pat] = to_match
            text2pat[to_match] = cur_pat
            found |= matchHelper(pat, patIdx+1, text, i+1, pat2text, text2pat)
            #del pat2text[cur_pat]
            #del text2pat[to_match]
            pat2text.pop(cur_pat, None)
            text2pat.pop(to_match, None)
            if found:
                return True
    return False


if __name__ == '__main__':
    pattern = raw_input()
    text = raw_input()
    print int(match(pattern, text))
