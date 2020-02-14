
def quick_sort( arr:list  = [4,8,3,6,23,90,2] ):

    n = len(arr)
    if n <= 1: return arr

    ret_arr = list(arr)

    # partition part of te algorithm

    pivot = arr[n - 1] # select the pivot (last number)

    print("the new pivot is: "+str(pivot))
    last_smal_index = -1

    for i, element in enumerate(ret_arr):

        #print("-- 1 The original array is: "+str(arr))

        if element <= pivot:
            #swap and increment pointer
            last_smal_index += 1
            # print("swaping small_index {} with index {}".format(str(last_smal_index), str(i)))
            ret_arr[last_smal_index], ret_arr[i] = ret_arr[i], ret_arr[last_smal_index] 

        else:
            # do nothing
            pass
        
        # print("-- 2 The result array is: "+str(arr))

    # use recursion to solve the problem
    lower = ret_arr[:last_smal_index]
    upper = ret_arr[last_smal_index + 1:]

    print(lower)
    print(upper)

    ret_arr = quick_sort(lower) + [pivot] + quick_sort(upper)
    
    return ret_arr

if __name__ == '__main__': 
    a = [1,3,7,5,2,8,0,4,3,78,3]
    sorted = quick_sort(a)
    print(a)
    print(sorted)

