"""
A caclulator
"""
from future import division

chars2 = "(2*789*789-456/987)*789+(321*789)-456+(321)-456 +(321*789  +(321))+(321+(321+(321-456+123)*789)+123-456) *789+123+(321  +(321+(321+123+123)-456*789/987+(321  +(321 +(321+(321+123 +(321+123*789))-456)))+123+(321*789+123+123-456)*789-456)+(321+(321+123)/987 )+123+123-456*789+(321/987*789 -456+(321*789)/987/987+(321+(321/987/987*789))))"

chars = "(2*789-456/987)*789  + 3"

Operator = set(['+', '-', '*', '/'])
Symbol = Operators | set(['(', ')'])
Number = (int, float)

def tokenize1(chars):
    for s in Symbol:
        chars = chars.replace(s, ' '+ s + ' ')
    return chars.split()

def to_eval(ops, nbs):
    """ Get top of ops stack, calcuate with two numebrs in nbs stack
    Args:
        ops, a stack to store operations
        nbs, a stack to store numbers
    Returns:
        None
    """
    # Add error handling here
    op = ops.pop()
    num1 = nbs.pop()
    num2 = nbs.pop()
    ans = 0
    if op == '+':
        ans = num2 + num1
    elif op == '-':
        ans = num2 - num1
    elif op == '*':
        ans = num2 * num1
    elif op == '/':
        if num1 == 0:
            ans = float('inf')
        else:
            ans = num2 / num1
    else:
        print ("ERROR")
    nbs.append(ans)
    

def caculate(expression):
    ops = []
    nbs = []
    pred = {'*':2, '/': 2, '+':1, '-':1}
    
    p, n = 0, len(expression)
    while p < n:
        
