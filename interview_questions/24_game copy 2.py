

# Property always holds: root.val = min(root.left.val, root.right.val)


from itertools import product, permutations


parenthesis = ["(", "(", ")", ")"]+[" "]*6


parenthesis_combinations = set(list(permutations(parenthesis, 6))) # 6 possible positions for the parenthesis


# for each parenthesis combination try each operation combination:
for parenthesis_list in parenthesis_combinations:
  

  # create the operation using eval:
  operation = "".join(
    [
      parenthesis_list[0],
      str(2), "*", 
      parenthesis_list[1], str(2), parenthesis_list[2], 
      "*", 
      parenthesis_list[3], str(3), parenthesis_list[4], 
      "*", str(4), 
      parenthesis_list[5]
    ])
  

  # if the operation is valid process it
  try:

    #if operation_list[0] is "*" and operation_list[1] is "*" and operation_list[2] is "*":
    result = eval(operation)
    #print("Operation: ", operation)
    #print("Result: ", result)
    print(parenthesis_list)
    

  except Exception:
    #print("Discarted: ", operation)
    pass

      
          
