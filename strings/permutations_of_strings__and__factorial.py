
"""
Given a string S. The task is to print all 
permutations of a given string.

Input:
The first line of input contains an integer T, 
denoting the number of test cases. Each test 
case contains a single string S in capital letter.

Output:
For each test case, print all permutations of 
a given string S with single space and all 
permutations should be in lexicographically 
increasing order.

Constraints:
1 ≤ T ≤ 10
1 ≤ size of string ≤ 5

Example:
Input:
2
ABC
ABSG

Output:
ABC ACB BAC BCA CAB CBA 

ABGS ABSG AGBS AGSB ASBG ASGB BAGS BASG BGAS 
BGSA BSAG BSGA GABS GASB GBAS GBSA GSAB GSBA 
SABG SAGB SBAG SBGA SGAB SGBA

Explanation:
Testcase 1: Given string ABC has permutations 
in 6 forms as ABC, ACB, BAC, BCA, CAB and CBA .
"""

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return n
    else:
        return n * factorial(n-1)


def permutation_of_strings(string_arr:str  = ["s","d","f","g"], init_i = None, final_i = None)-> int:

    n = len(string_arr)
    ret_arr = list()

    if n == 0:
        return 
    elif n == 1:
        return string_arr   

    if init_i == None or final_i == None:
        init_i = 0
        final_i = n - 1

    if  init_i == final_i:
        return string_arr
    else:

        for i in range(init_i, final_i + 1):

            #change the positions of the forst one with all the others
            string_arr[init_i], string_arr[i] = string_arr[i], string_arr[init_i] 

            #print("printing on stage init: {} and final: {}. the array is: {}".format(init_i, final_i, str(string_arr)))

            ret_arr += [permutation_of_strings(string_arr, init_i + 1, final_i)]

            # go back with the permutation
            string_arr[init_i], string_arr[i] = string_arr[i], string_arr[init_i] 


    return ret_arr


if __name__ == '__main__': 

    string = list("abc")
    permutations = permutation_of_strings(string)
    
    print("the permuttions are: "+str(permutations))



