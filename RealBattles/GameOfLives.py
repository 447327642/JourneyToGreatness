def print_matrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print mat[i][j],
        print
    print


def count_neighbors(x, y, mat):
    cnt = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            nx, ny = x + i, y + j
            if nx >= 0 and nx < len(mat) and ny >= 0 and ny < len(mat[0]):
                #print "mat[%d][%d] %d" % (nx, ny, mat[nx][ny])
                cnt += mat[nx][ny]
    cnt -= mat[x][y]
    return cnt 

def game_of_lives(mat, iters):
    rows, cols = len(mat), len(mat[0])
    it = 0
    while it < iters:
        tmp = [[0 for x in range(cols)] for y in range(rows)]
        for i in range(rows):
            for j in range(cols):
                nbs = count_neighbors(i, j, mat)
                #print 'i %d, j %d, cnt %d' % (i, j, nbs)
                if mat[i][j] == 1 and (nbs == 2 or nbs == 3):
                    tmp[i][j] = 0
                elif mat[i][j] == 0 and nbs == 3:
                    tmp[i][j] = 1
                else:
                    tmp[i][j] = mat[i][j]                    
        mat = tmp
        it += 1
    return mat

def game_of_lives2(mat, iters):
    rows, cols = len(mat), len(mat[0])
    it = 0
    while it < iters:
        changes = []
        for i in range(rows):
            for j in range(cols):
                nbs = count_neighbors(i, j, mat)
                if mat[i][j] == 1 and (nbs == 2 or nbs == 3):
                    # tmp[i][j] = 0
                    changes.append((i, j, 0))
                elif mat[i][j] == 0 and nbs == 3:
                    # tmp[i][j] = 1
                    changes.append((i, j, 1))
                # else:
                    # tmp[i][j] = mat[i][j]
        for item in changes:
            mat[item[0]][item[1]] = item[2]
        # mat = tmp
        it += 1
    return mat        
    
    
mat = [
    [1,1,0,0,0],
    [1,0,0,0,0],
    [0,0,0,1,0],
    [1,0,1,1,0],
    [0,1,1,0,0]
]

mat2 = [
    [0, 0, 1],
    [0, 1, 0],
    [0, 0, 0]
]

mat3 = [x[:] for x in mat] # copy of mat



print_matrix(game_of_lives2(mat, 1))
print_matrix(game_of_lives2(mat3, 2))
# print game_of_lives(mat, 2) == game_of_lives(mat3, 2)
