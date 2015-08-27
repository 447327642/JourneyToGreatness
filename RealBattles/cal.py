from __future__ import division
import sys

Symbol = set(['+', '-', '*', '/', '(', ')'])
Number = (int, float)

def tokenize(chars):
    """ Tokenize string into list
    Args:
        chars: a string
    Returns:
        a list of string
    """
    for s in Symbol:
        chars = chars.replace(s, ' '+ s + ' ')
    return chars.split()

def to_eval(ops, nbs):
    """ Get top of ops stack, calcuate with two numebrs in nbs stack
    Args:
        ops, a stack to store operations
        nbs, a stack to store numbers
    Returns:
        boolean: eval success or not
    """
    # Add error handling here
    if not ops or len(nbs) < 2:
        return False
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
        return False
    nbs.append(ans)
    return True
    
def calculate(expression):
    """ caculate input expression string
    Args:
        expression: string input
    Returns:
        None if ERROR
        float or inf if success

    ops, nbs: two stack to store operators and numbers
    pred: dict to store precedence
    """
    ops = []
    nbs = []
    pred = {'*':2, '/': 2, '+': 1, '-': 1, '(': 0, ')': 0}
    s = tokenize(expression)
    # this one is to fix 1+()2 case
    for tok in s:
        if tok in Symbol:
            if tok == '(':
                ops.append(tok)
            elif tok == ')':
                found_left = False
                while ops:
                    if ops[-1] == '(':
                        found_left = True
                        ops.pop()
                        break
                    if not to_eval(ops, nbs):
                        return 
                if not found_left:
                    return
            else: # operators keep calc until find lesser pred OP
                while ops and pred[ops[-1]] >= pred[tok]:
                    if not to_eval(ops, nbs):
                        return 
                ops.append(tok)
        else: # numbers or invalid symbols
            try:
                nbs.append(int(tok))
            except ValueError:
                try:
                    nbs.append(float(tok))
                except ValueError:
                    return

    while ops:
        if not to_eval(ops, nbs):
            return
    if len(nbs) != 1:
        return
    if not nbs:
        return
    return nbs[-1]
               

def main():
    for line in sys.stdin:
        ans = calculate(line[:-1])
        if not ans:
            print ("ERROR")
        else:
            print ("%.6f" % ans)


if __name__ == '__main__':
    # python cal.py < simple_input.txt > output1.txt
    main()
