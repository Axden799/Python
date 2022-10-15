def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0
    
    q = deque()
    C = len(grid)
    R = len(grid[0])
    num_islands = 0
    
    for c in range(C-1):
        for r in range(R-1):
            print(c, r)
            if grid[c][r] == '1': 
                q.append((c, r))
                print("APPEND")
                num_islands += 1
    
                while q:
                    c, r = q.popleft()
                    grid[c][r] = '0'

                    if c - 1 >= 0 and grid[c-1][r] == '1': 
                        q.append((c-1, r))
                        grid[c-1][r] = '0'
                    if c + 1 < C and grid[c+1][r] == '1': 
                        q.append((c+1, r))
                        grid[c+1][r] = '0'
                    if r - 1 >= 0 and grid[c][r-1] == '1': 
                        q.append((r-1, c))
                        grid[c][r-1] = '0'
                    if r + 1 < R and grid[c][r+1] == '1': 
                        q.append((r+1, c))
                        grid[c][r+1] = '0'
        
    print(grid)                   
                        
    return num_islands
                    