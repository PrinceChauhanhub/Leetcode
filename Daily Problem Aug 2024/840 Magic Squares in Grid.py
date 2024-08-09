class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(grid,r,c):
            St = set()
            for i in range(3):
                for j in range(3):
                    num = grid[r+i][c+j]
                    if num < 1 or num > 9 or num in St:
                        return False
                    else:
                        St.add(num)
                    
            ## check sum
            SUM = grid[r][c] + grid[r][c+1] + grid[r][c+2]
            
            for i in range(3):
                if grid[r+i][c] + grid[r+i][c+1] + grid[r+i][c+2] != SUM:
                    return False
                if grid[r][c+i] + grid[r+1][c+i] + grid[r+2][c+i] != SUM:
                    return False
            
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != SUM:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != SUM:
                return False
            
            return True

        rows = len(grid)
        cols = len(grid[0])

        count = 0
        for i in range(rows-2):
            for j in range(cols-2):
                if isMagic(grid,i,j):
                    count+=1
        
        return count