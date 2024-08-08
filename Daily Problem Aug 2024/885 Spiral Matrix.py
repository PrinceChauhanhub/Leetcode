class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, r_start: int, c_start: int) -> List[List[int]]:
        directions = [
        (0, 1),   # EAST
        (1, 0),   # SOUTH
        (0, -1),  # WEST
        (-1, 0)   # NORTH
        ]
    
        result = []
        step = 0  
        dir = 0  
        result.append([r_start, c_start])

        while len(result) < rows * cols:
            if dir == 0 or dir == 2:
                step += 1

            for _ in range(step):
                r_start += directions[dir][0]
                c_start += directions[dir][1]

                if 0 <= r_start < rows and 0 <= c_start < cols: 
                    result.append([r_start, c_start])

            dir = (dir + 1) % 4  

        return result