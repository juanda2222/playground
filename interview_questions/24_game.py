

# Property always holds: root.val = min(root.left.val, root.right.val)


from itertools import product, permutations


class Solution:

    def judgePoint24(self, nums: list) -> bool:

      operations = ["*", "/", "+", "-"]
      parenthesis_combinations = (
        (' ', ' ', ' ', ' ', ' ', ' '),
        (' ', ' ', ' ', '(', ' ', ')'),
        ('(', ' ', ')', ' ', ' ', ' '),
        ('(', ' ', ')', '(', ' ', ')'),
        (' ', '(', ' ', ' ', ')', ' '),
        ('(', ' ', ' ', ' ', ')', ' '),
        (' ', '(', ' ', ' ', ' ', ')'),
        #(' ', '((', ' ', ' ', ')', ')'),
        #(' ', '(', ' ', '(', ' ', '))'),
        #('(', '(', ' ', ' ', '))', ' '),
        #('((', ' ', ')', ' ', ')', ' '),
      )

      number_permutations = set(list(permutations(nums))) # use a little bit of memory to avoid swaps between repeated numbers
      operation_combinations = set(list(product(operations, repeat=3)))  # 3 possible operations
      #parenthesis_combinations = set(list(permutations(parenthesis, 6))) # 6 possible positions for the parenthesis
      all_combinations = set(list(product(number_permutations, operation_combinations, parenthesis_combinations)))

      
      # for each parenthesis combination try each operation combination:
      for number_list, operation_list, parenthesis_list in all_combinations:
        
      
        # create the operation using eval:
        operation = "".join(
          [
            parenthesis_list[0],
            str(number_list[0]), operation_list[0], 
            parenthesis_list[1], str(number_list[1]), parenthesis_list[2], 
            operation_list[1], 
            parenthesis_list[3], str(number_list[2]), parenthesis_list[4], 
            operation_list[2], str(number_list[3]), 
            parenthesis_list[5]
          ])
        

        # if the operation is valid process it
        try:

          #if operation_list[0] is "*" and operation_list[1] is "*" and operation_list[2] is "*":
          result = eval(operation)
          print("Operation: ", operation)
          print("Result: ", result)
          rounded = round(result, 10)
          print("Round result: ", rounded)

          if rounded == 24:
            return True

        except Exception:
          #print("Discarted: ", operation)
          pass

      return False

      
from operator import truediv, mul, add, sub

class SolutionOfficial(object):
    def judgePoint24(self, A):
        print(A)
        if not A: return False
        if len(A) == 1: return abs(A[0] - 24) < 1e-6

        for i in range(len(A)):
            for j in range(len(A)):
                if i != j:
                    B = [A[k] for k in range(len(A)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if (op is add or op is mul) and j > i: continue
                        if op is not truediv or A[j]:
                            B.append(op(A[i], A[j]))
                            if self.judgePoint24(B): return True
                            B.pop()
        return False
          

num = [1,1,7,7] # false
num_list = [4, 1, 8, 7]
num_list2 = [1, 3, 4, 6] # True
num_list3 = [1, 2, 1, 2]
num_list4 = [8,1,6,6]
#sol = Solution()
#ret = sol.judgePoint24(num)
#print("Return:", ret)

# official
sol = SolutionOfficial()
ret = sol.judgePoint24(num)
print("Return oficial:", ret)