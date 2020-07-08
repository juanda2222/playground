
from itertools import product
import numpy as np

class Solution:

    def uniquePaths(self, m: int, n: int) -> int:

        map_matrix = np.zeros((m , n))

        #fill the matrix with the straight lines:
        for row_i in range(n):
            map_matrix[0][row_i] = 1

        print(map_matrix)

        #fill the matrix with the straight lines:
        for col_i in range(m):
            map_matrix[col_i][0] = 1

        ## fill the rest:
        for row_i in range(1, n):
            for col_i in range(1, m):
                map_matrix[col_i][row_i] = map_matrix[col_i - 1][row_i] + map_matrix[col_i][row_i - 1]

        return int(map_matrix[-1][-1])
        

sol = Solution()
print(sol.uniquePaths(7, 3))