names = ["wilson", "tom", "hello", "what", "david", "k", "sa", "wang", "kai"]

width = 8

def put_names(names, width):
    assert(max(len(name) for name in names) <= width)
    names = sorted(names, key=len, reverse=True)
    result = []
    for name in names:
        new_line = True
        for i in range(len(result)):
            if width - result[i] >= len(name):
                result[i] += len(name)
                new_line = False
                break
        if new_line:
            result.append(len(name))
    print result
    return len(result)
        

print put_names(names, width)
