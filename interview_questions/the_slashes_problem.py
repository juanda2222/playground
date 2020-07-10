

# Property always holds: root.val = min(root.left.val, root.right.val)


from math import sqrt
import numpy as np

class Solution:

    def Regions(self, Vertices: int, Edges:int) :  
        n_regions = Edges + 2 - Vertices;  
        return n_regions;  

    def regionsBySlashes(self, grid: list) -> int:

        # create holding matrix
        l = len(grid)
        matrix_grid = np.empty(( l,  l ), dtype='object')
        
        # fill the matrix:
        for k in range(l):
            for j in range(l):
                matrix_grid[j][k] = grid[j][k]

        print(matrix_grid)

        # here 0 means not analized yet
        # 1 means the top path has been analized
        # 2 means both paths have been analized
        
        # generate the unique path matrix
        pairing_matrix = []
        for i in range(l):
            pairing_matrix.append(np.arange(l * i, l * (i+1)))
        pairing_matrix = np.array(pairing_matrix)

        print(pairing_matrix)

        # process the id matrix
        for j in pairing_matrix:
            for j in pairing_matrix:
                pass
            
            #depending on the symbol join to the bigger one
        
        
                #special case 1 (/ on the upper left corner OR the bottom rigth)

                #special case 2 (\\ on the rigth upper corner OR the bottom left)

                #follow the path counter clockwise starting from top


        return 1

slash_list = [
  "\\/",
  "/\\"
]

slash_list2 = [
  "/\\",
  "\\/"
]

slash_list3 = [
  "//",
  "/ "
]

slash_list4 = [
    "/\\/\\",
    "/\\\\/",
    "/\\\\/",
    "    "
]
sol = Solution()
ret = sol.regionsBySlashes(slash_list4)
print("Return:", ret)