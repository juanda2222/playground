
def merge_sort( arr:list  = [4,8,3,6,23,90,2] ) -> list:
    
    print("received: "+str(arr))

    if len(arr) <= 0 : raise ValueError("Array too small")
    if len(arr) <= 1 : return arr
    ret_arr = list(arr)


    middle_index = int(len(ret_arr)/2)

    sorted_lower = ret_arr[:middle_index] # get the lower half
    sorted_upper = ret_arr[middle_index:] # get the upper half


    sorted_lower = merge_sort(sorted_lower) # sort them using recursion
    sorted_upper = merge_sort(sorted_upper) # sort them using recursion

    

    # Copy data to the return array asuming they are sorted this is a merging function
    i = j = 0 # i for the lower, j for the upper
    for k in range(len(ret_arr)): 
        print("i: "+str(i)+", j: "+str(j))
        
        #check if the indexes are overflown
        if i >= len(sorted_lower): # lower index overflow
            ret_arr[k] = sorted_upper[j]
            j+=1
        elif j >= len(sorted_upper): # upper index overflow
            ret_arr[k] = sorted_lower[i]
            i+=1
        
        # compare both vecs to orginize them
        elif sorted_lower[i] < sorted_upper[j]: 
            ret_arr[k] = sorted_lower[i] 
            i+=1
        else: 
            ret_arr[k] = sorted_upper[j] 
            j+=1
        

    print("returned: "+str(ret_arr))

    return ret_arr



if __name__ == '__main__': 

    a = [1,5,112,23,45,32,123,43]
    sorted = merge_sort(a)
    print(a)
    print(sorted)

