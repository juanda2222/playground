
from itertools import product
import numpy as np


class Solution:
    def is_point_in_line(self, point:list, m, b) -> bool:
        return point[1] == m * point[0] + b # x is pooint[0]

    def maxPoints(self, points) -> int:
        
        if len(points) <= 0 :
            return 0

        max_count = 1

        # calculate m and b comparing each point
        for ref_point in points:
            for point in points:

                
                x_ref = ref_point[0]
                y_ref = ref_point[1]
                x = point[0]
                y = point[1]
                
                # calculate line
                print(point)
                print(ref_point)
                
                count = 0 # the starting point

                # count diferent if we fount a vertical line:
                try:
                
                    m = (y_ref - y) / (x_ref - x)
                    b = y_ref - (m * x_ref)

                    # count the numpers of points that are inside the line:
                    for points_to_count in points:
                        if self.is_point_in_line(points_to_count, m, b):
                            count += 1

                # means a vertical line the counting process is diferent:
                except ZeroDivisionError:
                    
                    # count the numpers of points that indetermine "b"
                    for points_to_count in points:
                        
                        try:
                            m = (y_ref - points_to_count[1]) / (x_ref - points_to_count[0])
                            b = y_ref - (m * x_ref)

                        except ZeroDivisionError:
                            count += 1                            

                if count > max_count:
                    max_count = count

        return max_count
        

sol = Solution()
print(sol.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))
print(sol.maxPoints( [[0,0],[0,0]] ))