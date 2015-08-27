import os
# write file info into a class
path = "/Users/wilbeibi/Dropbox/Programs/Python/PlayGround/test_walk"
hash32 = lambda value: hash(value) & 0xffffffff

def hash32_1(filename):
    with open(filename) as f:
        content = f.read()
        return hash(content) & 0xffffffff


def get_all_files(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for name in files:
            fullname = os.path.join(root, name)
            yield (fullname, os.path.getsize(fullname))

def get_all_files2(path):
    file_list = []
    def dfs(path):
        contents = os.listdir(path)
        for item in contents:
            if os.path.isdir(item):
                dfs(item)
            else:
                # if it is hard link/symbol link
                file_list.append(os.path.realpath(item))
                # if not enough memory, use yield
    dfs(path)
    return file_list

#print get_all_files(path)
print get_all_files2(path)


#print get_all_files(path)

file_by_size_dic = {}
for file_info in get_all_files(path):
    if file_info[1] in file_by_size_dic:
        file_by_size_dic[file_info[1]].append(file_info[0])
    else:
        file_by_size_dic[file_info[1]] = [file_info[0]]

#print file_by_size_dic



def unique(file_list, hash_func = hash32, read_size = None):
    """
    Args:
        file_list: a list of file name string
    Return:
        unique_list: a list of list of identical file (string) for given file_list
    """
    result = {} # a empty dictionary with 32 possible key
    for fname in file_list:
        with open(fname, 'r') as f:
            if read_size != None:
                buff = f.read(read_size)
            else:
                buff = f.read()

            if hash_func(buff) not in result:
                result[hash_func(buff)] = [fname]
            else:
                result[hash_func(buff)].append(fname)

    unique_list = [result[key] for key in result]
    #print 'unique list', unique_list
    return unique_list


for size_key in file_by_size_dic:
    file_by_size_dic[size_key] = unique(file_by_size_dic[size_key])


res = []
for k, v in file_by_size_dic.items():
    for identical in v:
        res.append(identical)
    #for 2d_list in v:
     #   print 2d_list
#print res
