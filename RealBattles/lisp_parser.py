
def tokenize(chars):
    """ Convert a string of characters into a list of tokens.
    """
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program):
    """ Read a Scheme expression from a string.
    """
    return read_from_tokens(tokenize(program))

def read_from_tokens(tokens):
    """ Read an expression from a sequence of tokens.
    """
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF while reading')
    token = tokens.pop(0)
    if '(' == token:
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif ')' == token:
        raise SyntaxError('unexpected )')
    else:
        return atom(token)

Symbol = str
List = list
Number = (int, float)
def atom(token):
    """ Numbers become numbers; every other tokens is a symbol
    """
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return Symbol(token)

Env = dict
def standard_env():
    """ An environment with soem Scheme stanard procedures
    """
    import math, operator as op
    env = Env()
    env.update({
        'add': op.add,
        'sub': op.sub,
        'mul': op.mul,
        'div': op.div,
    })
    return env

global_env = standard_env()

def to_eval(x, env=global_env):
    """ Evaluate an expression in an environment.
    """
    print ("to_eval", x, )
    if not isinstance(x, List) and x in env:
        print (' ', env[x])
    if isinstance(x, Symbol):
        return env[x]
    elif not isinstance(x, List): # constant literal
        return x
    
    elif x[0] == 'let':
        (_, var, exp) = x[:3]
        env[var] = to_eval(exp, env)
        return to_eval(x[3:], env)
    else:
        proc = to_eval(x[0], env)
        args = [to_eval(arg, env) for arg in x[1:]]
        return proc(*args)
        
 
def evaluate(string):
    print (to_eval(parse(string)))


strs = ["(add 1 2)",
        "(mul 3 (add 2 3))",
        "(let x 2 (mul x 5))",
        "(let x 2 (mul x (let x 3 y 4 (add x y))))"
        ]

evaluate(strs[2])

