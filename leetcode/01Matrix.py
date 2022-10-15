from collections import deque
import math

def updateMatrix(mat):
    output = []
    ROW = len(mat) - 1
    COL = len(mat[0]) - 1
    def dfs(r, c):
        nonlocal count
        print(r, c)
        print(mat[r][c])
        if mat[r][c] == 0:
            print("YES")
            print(count)
            return count
        else:
            count += 1
            if r > 0: dfs(r-1, c)
            if c > 0: dfs(r, c-1)
            if r < ROW: dfs(r+1, c)
            if c > COL: dfs(r, c+1)
            
    for x in range(len(mat)):
        output.append([])
        for y in range(len(mat[0])):
            count = 0
            zero_dist = dfs(x, y)
            output[x].append(zero_dist)
            print("DONE")
    return output



def updateMatrixQueue(mat):
    m, n = len(mat), len(mat[0])
    DIR = [0, 1, 0, -1, 0]

    q = deque([])
    for r in range(m):
        for c in range(n):
            if mat[r][c] == 0:
                q.append((r, c))
            else:
                mat[r][c] = -1  # Marked as not processed yet!

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + DIR[i], c + DIR[i + 1]
            if nr < 0 or nr == m or nc < 0 or nc == n or mat[nr][nc] != -1: continue
            mat[nr][nc] = mat[r][c] + 1
            q.append((nr, nc))
    return mat
            

def bestMatrixQueue(mat):
    m, n = len(mat), len(mat[0])

    for x in range(m):
        for y in range(n):
            if mat[m][n] > 0:
                top = mat[x-1][y] if x > 0 else math.inf
                left = mat[x][y-1] if y > 0 else math.inf
                mat[x][y] = min(top, left) + 1

    for x in range(m - 1, -1, -1):
        for y in range(n - 1, -1, -1):
            if mat[m][n] > 0:
                bottom = mat[x+1][y] if x < m - 1 else math.inf
                right = mat[x][y+1] if y < m-1 else math.inf
                mat[x][y] = min(mat[x][y], bottom, right)

    return mat

        


